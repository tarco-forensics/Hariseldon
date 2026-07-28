# -*- coding: utf-8 -*-
"""
T2SAIM World Cup 2026 Group Stage Simulator
===========================================
Simulates the remaining matches of the 2026 World Cup Group Stage (12 groups, 48 teams)
using two different models:
1. Model 1 (Static/FIFA Rank Model): Pure Poisson simulation based on constant team strengths.
2. Model 2 (Seldon/Amnesia Model): Poisson simulation with the T2SAIM Amnesia protocol (lambda=0.25)
   updating team strengths dynamically after each Matchday.

Saves results to 'B:\\Hariseldon\\dashboards\\world_cup_sim_results.json'.
"""

import os
import sys
import json
import math
import random
from datetime import datetime

# Set seed for reproducibility
random.seed(42)

# Group structure & team stats
# Base strengths (guc) and FIFA ranks
TAKIMLAR_WC = {
    "A": [
        {"ad": "🇲🇽 Meksika", "guc": 0.87, "fifa": 14},
        {"ad": "🇿🇦 G. Afrika", "guc": 0.73, "fifa": 59},
        {"ad": "🇰🇷 G. Kore", "guc": 0.82, "fifa": 25},
        {"ad": "🇨🇿 Çekya", "guc": 0.79, "fifa": 40}
    ],
    "B": [
        {"ad": "🇨🇦 Kanada", "guc": 0.78, "fifa": 49},
        {"ad": "🇨🇭 İsviçre", "guc": 0.84, "fifa": 19},
        {"ad": "🇶🇦 Katar", "guc": 0.75, "fifa": 58},
        {"ad": "🇧🇦 Bosna Hersek", "guc": 0.74, "fifa": 68}
    ],
    "C": [
        {"ad": "🇧🇷 Brezilya", "guc": 0.96, "fifa": 1},
        {"ad": "🇲🇦 Fas", "guc": 0.89, "fifa": 14},
        {"ad": "🇭🇹 Haiti", "guc": 0.68, "fifa": 83},
        {"ad": "🏴󠁧󠁢󠁳󠁣󠁴󠁿 İskoçya", "guc": 0.78, "fifa": 42}
    ],
    "D": [
        {"ad": "🇺🇸 ABD", "guc": 0.88, "fifa": 11},
        {"ad": "🇵🇾 Paraguay", "guc": 0.76, "fifa": 48},
        {"ad": "🇦🇺 Avustralya", "guc": 0.81, "fifa": 27},
        {"ad": "🇹🇷 Türkiye", "guc": 0.83, "fifa": 28}
    ],
    "E": [
        {"ad": "🇩🇪 Almanya", "guc": 0.91, "fifa": 5},
        {"ad": "🇨🇼 Curaçao", "guc": 0.65, "fifa": 86},
        {"ad": "🇨🇮 Fildişi Sahili", "guc": 0.79, "fifa": 50},
        {"ad": "🇪🇨 Ekvador", "guc": 0.82, "fifa": 32}
    ],
    "F": [
        {"ad": "🇳🇱 Hollanda", "guc": 0.92, "fifa": 12},
        {"ad": "🇯🇵 Japonya", "guc": 0.85, "fifa": 18},
        {"ad": "🇹🇳 Tunus", "guc": 0.75, "fifa": 41},
        {"ad": "🇸🇪 İsveç", "guc": 0.81, "fifa": 22}
    ],
    "G": [
        {"ad": "🇧🇪 Belçika", "guc": 0.94, "fifa": 10},
        {"ad": "🇪🇬 Mısır", "guc": 0.79, "fifa": 36},
        {"ad": "🇮🇷 İran", "guc": 0.83, "fifa": 21},
        {"ad": "🇳🇿 Yeni Zelanda", "guc": 0.65, "fifa": 80}
    ],
    "H": [
        {"ad": "🇪🇸 İspanya", "guc": 0.95, "fifa": 8},
        {"ad": "🇨🇻 Yeşil Burun", "guc": 0.72, "fifa": 72},
        {"ad": "🇸🇦 S. Arabistan", "guc": 0.74, "fifa": 53},
        {"ad": "🇺🇾 Uruguay", "guc": 0.90, "fifa": 16}
    ],
    "I": [
        {"ad": "🇫🇷 Fransa", "guc": 0.97, "fifa": 3},
        {"ad": "🇸🇳 Senegal", "guc": 0.84, "fifa": 20},
        {"ad": "🇳🇴 Norveç", "guc": 0.82, "fifa": 44},
        {"ad": "🇮🇶 Irak", "guc": 0.73, "fifa": 55}
    ],
    "J": [
        {"ad": "🇦🇷 Arjantin", "guc": 0.98, "fifa": 2},
        {"ad": "🇩🇿 Cezayir", "guc": 0.78, "fifa": 37},
        {"ad": "🇦🇹 Avusturya", "guc": 0.82, "fifa": 26},
        {"ad": "🇯🇴 Ürdün", "guc": 0.72, "fifa": 78}
    ],
    "K": [
        {"ad": "🇵🇹 Portekiz", "guc": 0.94, "fifa": 9},
        {"ad": "🇺🇿 Özbekistan", "guc": 0.74, "fifa": 64},
        {"ad": "🇨🇴 Kolombiya", "guc": 0.89, "fifa": 13},
        {"ad": "🇨🇩 Demokratik Kongo", "guc": 0.74, "fifa": 62}
    ],
    "L": [
        {"ad": "🏴󠁧󠁢󠁥󠁮󠁧󠁿 İngiltere", "guc": 0.95, "fifa": 4},
        {"ad": "🇭🇷 Hırvatistan", "guc": 0.90, "fifa": 15},
        {"ad": "🇬🇭 Gana", "guc": 0.74, "fifa": 60},
        {"ad": "🇵🇦 Panama", "guc": 0.75, "fifa": 65}
    ]
}

# Matchday 1 Actual Results
# Scores formatted as: (goals_team_A, goals_team_B)
MATCHDAY_1_RESULTS = {
    "A": {
        (0, 1): (2, 0),  # Mexico vs South Africa
        (2, 3): (2, 1)   # South Korea vs Czechia
    },
    "B": {
        (0, 3): (1, 1),  # Canada vs Bosnia and Herzegovina
        (2, 1): (1, 1)   # Qatar vs Switzerland (Wait! Qatar vs Switzerland is 2 vs 1)
    },
    "C": {
        (0, 1): (1, 1),  # Brazil vs Morocco
        (3, 2): (1, 0)   # Scotland vs Haiti
    },
    "D": {
        (0, 1): (4, 1),  # USA vs Paraguay
        (2, 3): (2, 0)   # Australia vs Turkey
    },
    "E": {
        (0, 1): (7, 1),  # Germany vs Curaçao
        (2, 3): (1, 0)   # Ivory Coast vs Ecuador
    },
    "F": {
        (0, 1): (2, 2),  # Netherlands vs Japan
        (3, 2): (5, 1)   # Sweden vs Tunisia
    },
    "G": {
        (0, 1): (1, 1),  # Belgium vs Egypt
        (2, 3): (2, 2)   # Iran vs New Zealand
    },
    "H": {
        (0, 1): (0, 0),  # Spain vs Cape Verde
        (2, 3): (1, 1)   # Saudi Arabia vs Uruguay (Wait! Saudi vs Uruguay is 2 vs 3)
    },
    "I": {
        (0, 1): (3, 1),  # France vs Senegal
        (2, 3): (4, 1)   # Norway vs Iraq
    },
    "J": {
        (0, 1): (3, 0),  # Argentina vs Algeria
        (2, 3): (3, 1)   # Austria vs Jordan
    },
    "K": {
        (0, 3): (1, 1),  # Portugal vs DR Congo
        (2, 1): (2, 0)   # Colombia vs Uzbekistan (Colombia 2-0 Uzbekistan - simulated default)
    },
    "L": {
        (0, 1): (3, 2),  # England vs Croatia (England 3-2 Croatia)
        (2, 3): (1, 1)   # Ghana vs Panama (Ghana 1-1 Panama - simulated default)
    }
}

# Remaining Fixtures
FIXTURES = {
    2: [[0, 2], [1, 3]],  # Matchday 2
    3: [[0, 3], [1, 2]]   # Matchday 3
}

def poisson_sample(lmbda):
    """Knuth's algorithm for Poisson sampling"""
    L = math.exp(-lmbda)
    k = 0
    p = 1.0
    while p > L:
        k += 1
        p *= random.random()
    return max(0, k - 1)

def run_simulation(model_version, iterations=10000):
    """Runs Monte Carlo simulations for the tournament group stage"""
    # Track metrics for each team
    # Each entry will store: {ad, group, s1, s2, s3, s4, qualified, qualified_direct, qualified_3rd}
    stats = {}
    for g, teams in TAKIMLAR_WC.items():
        for t in teams:
            stats[t["ad"]] = {
                "ad": t["ad"],
                "group": g,
                "fifa": t["fifa"],
                "s1": 0, "s2": 0, "s3": 0, "s4": 0,
                "qualified": 0,
                "qualified_direct": 0,
                "qualified_3rd": 0
            }

    # Run simulations
    for _ in range(iterations):
        # Temp variables for this iteration
        # group_points[group][team_idx]
        # group_gd[group][team_idx]
        # group_gf[group][team_idx]
        # team_strengths[team_name]
        group_points = {g: [0]*4 for g in TAKIMLAR_WC}
        group_gd = {g: [0]*4 for g in TAKIMLAR_WC}
        group_gf = {g: [0]*4 for g in TAKIMLAR_WC}
        
        # Initialize strengths for this iteration
        team_strengths = {}
        for g, teams in TAKIMLAR_WC.items():
            for i, t in enumerate(teams):
                team_strengths[t["ad"]] = t["guc"]

        # 1. Process Matchday 1 (Fixed Actual Results)
        for g, matches in MATCHDAY_1_RESULTS.items():
            teams = TAKIMLAR_WC[g]
            for (idx_A, idx_B), (goals_A, goals_B) in matches.items():
                # Update stats
                group_gf[g][idx_A] += goals_A
                group_gf[g][idx_B] += goals_B
                group_gd[g][idx_A] += (goals_A - goals_B)
                group_gd[g][idx_B] += (goals_B - goals_A)
                if goals_A > goals_B:
                    group_points[g][idx_A] += 3
                elif goals_A < goals_B:
                    group_points[g][idx_B] += 3
                else:
                    group_points[g][idx_A] += 1
                    group_points[g][idx_B] += 1
                
                # Apply Amnesia (lambda=0.25) to update strengths after MD1 for MD2
                if model_version == 2:
                    # Determine performance
                    perf_A = 1.0 if goals_A > goals_B else (0.5 if goals_A == goals_B else 0.0)
                    perf_B = 1.0 if goals_B > goals_A else (0.5 if goals_A == goals_B else 0.0)
                    
                    team_strengths[teams[idx_A]["ad"]] = teams[idx_A]["guc"] * 0.75 + perf_A * 0.25
                    team_strengths[teams[idx_B]["ad"]] = teams[idx_B]["guc"] * 0.75 + perf_B * 0.25

        # 2. Simulate Matchday 2
        for g, teams in TAKIMLAR_WC.items():
            for idx_A, idx_B in FIXTURES[2]:
                # Goals simulated using Poisson
                lmbda_A = team_strengths[teams[idx_A]["ad"]] * 1.6
                lmbda_B = team_strengths[teams[idx_B]["ad"]] * 1.6
                goals_A = poisson_sample(lmbda_A)
                goals_B = poisson_sample(lmbda_B)

                group_gf[g][idx_A] += goals_A
                group_gf[g][idx_B] += goals_B
                group_gd[g][idx_A] += (goals_A - goals_B)
                group_gd[g][idx_B] += (goals_B - goals_A)
                if goals_A > goals_B:
                    group_points[g][idx_A] += 3
                elif goals_A < goals_B:
                    group_points[g][idx_B] += 3
                else:
                    group_points[g][idx_A] += 1
                    group_points[g][idx_B] += 1

                # Apply Amnesia to update strengths after MD2 for MD3
                if model_version == 2:
                    perf_A = 1.0 if goals_A > goals_B else (0.5 if goals_A == goals_B else 0.0)
                    perf_B = 1.0 if goals_B > goals_A else (0.5 if goals_A == goals_B else 0.0)
                    
                    # Update based on previous strength (MD2 strength)
                    s_md2_A = team_strengths[teams[idx_A]["ad"]]
                    s_md2_B = team_strengths[teams[idx_B]["ad"]]
                    team_strengths[teams[idx_A]["ad"]] = s_md2_A * 0.75 + perf_A * 0.25
                    team_strengths[teams[idx_B]["ad"]] = s_md2_B * 0.75 + perf_B * 0.25

        # 3. Simulate Matchday 3
        for g, teams in TAKIMLAR_WC.items():
            for idx_A, idx_B in FIXTURES[3]:
                # Goals simulated using Poisson
                lmbda_A = team_strengths[teams[idx_A]["ad"]] * 1.6
                lmbda_B = team_strengths[teams[idx_B]["ad"]] * 1.6
                goals_A = poisson_sample(lmbda_A)
                goals_B = poisson_sample(lmbda_B)

                group_gf[g][idx_A] += goals_A
                group_gf[g][idx_B] += goals_B
                group_gd[g][idx_A] += (goals_A - goals_B)
                group_gd[g][idx_B] += (goals_B - goals_A)
                if goals_A > goals_B:
                    group_points[g][idx_A] += 3
                elif goals_A < goals_B:
                    group_points[g][idx_B] += 3
                else:
                    group_points[g][idx_A] += 1
                    group_points[g][idx_B] += 1

        # 4. Resolve Group Standings & Third-Place Ranking
        third_placed_teams = []
        for g, teams in TAKIMLAR_WC.items():
            # Create team records
            recs = []
            for i, t in enumerate(teams):
                recs.append({
                    "ad": t["ad"],
                    "idx": i,
                    "p": group_points[g][i],
                    "gd": group_gd[g][i],
                    "gf": group_gf[g][i],
                    "rand": random.random()  # Tie breaker
                })
            
            # Sort by Points, GD, GF, Rand
            recs.sort(key=lambda x: (x["p"], x["gd"], x["gf"], x["rand"]), reverse=True)

            # Record positions
            stats[recs[0]["ad"]]["s1"] += 1
            stats[recs[1]["ad"]]["s2"] += 1
            stats[recs[2]["ad"]]["s3"] += 1
            stats[recs[3]["ad"]]["s4"] += 1

            # Top 2 qualify directly
            stats[recs[0]["ad"]]["qualified_direct"] += 1
            stats[recs[0]["ad"]]["qualified"] += 1
            stats[recs[1]["ad"]]["qualified_direct"] += 1
            stats[recs[1]["ad"]]["qualified"] += 1

            # Third placed team goes to global pool
            third_placed_teams.append({
                "ad": recs[2]["ad"],
                "p": recs[2]["p"],
                "gd": recs[2]["gd"],
                "gf": recs[2]["gf"],
                "rand": random.random()
            })

        # Rank third-placed teams globally
        third_placed_teams.sort(key=lambda x: (x["p"], x["gd"], x["gf"], x["rand"]), reverse=True)

        # Top 8 qualify
        for i in range(8):
            t_ad = third_placed_teams[i]["ad"]
            stats[t_ad]["qualified_3rd"] += 1
            stats[t_ad]["qualified"] += 1

    # Format output
    result_list = []
    for k, v in stats.items():
        result_list.append({
            "ad": v["ad"],
            "group": v["group"],
            "fifa": v["fifa"],
            "s1": round((v["s1"] / iterations) * 100, 2),
            "s2": round((v["s2"] / iterations) * 100, 2),
            "s3": round((v["s3"] / iterations) * 100, 2),
            "s4": round((v["s4"] / iterations) * 100, 2),
            "qualified_direct": round((v["qualified_direct"] / iterations) * 100, 2),
            "qualified_3rd": round((v["qualified_3rd"] / iterations) * 100, 2),
            "qualified": round((v["qualified"] / iterations) * 100, 2)
        })

    return result_list

def main():
    print("[+] Starting World Cup 2026 Simulations...")
    
    # 1. Run Model 1 (Static Model: lambda=0.0)
    print(" - Simulating Model 1 (Static/FIFA Rank)...")
    model_1_results = run_simulation(model_version=1, iterations=10000)

    # 2. Run Model 2 (Seldon Amnesia Model: lambda=0.25)
    print(" - Simulating Model 2 (Seldon/Amnesia)...")
    model_2_results = run_simulation(model_version=2, iterations=10000)

    # Output structure
    output_data = {
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "matchday": 1,
        "model_1": model_1_results,
        "model_2": model_2_results
    }

    # Ensure directories exist
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(BASE_DIR, "dashboards")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, "world_cup_sim_results.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)

    print(f"[+] Simulation complete! Results saved to: {output_file}")

if __name__ == "__main__":
    main()
