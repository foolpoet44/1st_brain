# Extracted Knowledge from Conv: bc54d51c-655f-4aad-bd85-bd80a1ef2113

**Date**: 2025-10-22T02:23:57.433291Z

### Extracted Code (python)

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
# plt.rcParams['font.family'] = 'AppleGothic'  # Mac
plt.rcParams['axes.unicode_minus'] = False

# =============================================================================
# 분석 4-1: 17개 역량별 t-test 수행
# =============================================================================

print("\n" + "="*80)
print("=== 24년-25년 역량별 평균변화 검증 (Independent t-test) ===")
print("="*80)

ttest_results = []

for comp in COMPETENCY_LIST:
    # 2024년, 2025년 데이터 추출
    scores_2024 = df_other_2024[comp].dropna()
    scores_2025 = df_other_2025[comp].dropna()
    
    # t-test 수행 (독립표본 t검정)
    t_stat, p_value = stats.ttest_ind(scores_2025, scores_2024)
    
    # 평균 및 표준편차
    mean_2024 = scores_2024.mean()
    mean_2025 = scores_2025.mean()
    std_2024 = scores_2024.std()
    std_2025 = scores_2025.std()
    
    # 변화량 및 효과크기 (Cohen's d)
    change = mean_2025 - mean_2024
    pooled_std = np.sqrt(((len(scores_2024)-1)*std_2024**2 + (len(scores_2025)-1)*std_2025**2) / 
                         (len(scores_2024) + len(scores_2025) - 2))
    cohens_d = change / pooled_std if pooled_std != 0 else 0
    
    # 유의성 판단
    if p_value < 0.001:
        significance = '***'
    elif p_value < 0.01:
        significance = '**'
    elif p_value < 0.05:
        significance = '*'
    else:
        significance = 'ns'
    
    ttest_results.append({
        '역량': comp,
        '2024_평균': mean_2024,
        '2024_표준편차': std_2024,
        '2024_N': len(scores_2024),
        '2025_평균': mean_2025,
        '2025_표준편차': std_2025,
        '2025_N': len(scores_2025),
        '변화량': change,
        't값': t_stat,
        'p값': p_value,
        "Cohen's d": cohens_d,
        '유의성': significance
    })

# DataFrame 생성
df_ttest = pd.DataFrame(ttest_results)

# p값 기준 정렬 (유의한 결과 우선)
df_ttest_sorted = df_ttest.sort_values('p값').reset_index(drop=True)

# 결과 출력
print(f"\n{'역량':<15} {'2024평균':>8} {'2025평균':>8} {'변화량':>8} {'t값':>8} {'p값':>10} {'효과크기':>8} {'유의성':>6}")
print("-"*80)
for _, row in df_ttest_sorted.iterrows():
    print(f"{row['역량']:<15} {row['2024_평균']:>8.3f} {row['2025_평균']:>8.3f} "
          f"{row['변화량']:>8.3f} {row['t값']:>8.3f} {row['p값']:>10.6f} "
          f"{row['Cohen\'s d']:>8.3f} {row['유의성']:>6}")

# 유의성 요약
sig_count = len(df_ttest[df_ttest['p값'] < 0.05])
print(f"\n유의한 변화를 보인 역량: {sig_count}개 / {len(COMPETENCY_LIST)}개")
print(f"※ ***: p<0.001, **: p<0.01, *: p<0.05, ns: not significant")

# =============================================================================
# 시각화 1: 역량별 변화량 바차트 (유의성 표시)
# =============================================================================

fig, ax = plt.subplots(figsize=(14, 10))

# 변화량 기준 정렬
df_ttest_plot = df_ttest.sort_values('변화량', ascending=True).reset_index(drop=True)

# 색상 설정 (유의성에 따라)
colors = []
for sig in df_ttest_plot['유의성']:
    if sig == '***':
        colors.append('#d62728')  # 빨강 (p<0.001)
    elif sig == '**':
        colors.append('#ff7f0e')  # 주황 (p<0.01)
    elif sig == '*':
        colors.append('#2ca02c')  # 초록 (p<0.05)
    else:
        colors.append('#7f7f7f')  # 회색 (ns)

# 바차트
bars = ax.barh(df_ttest_plot['역량'], df_ttest_plot['변화량'], color=colors, alpha=0.8)

# 0 기준선
ax.axvline(x=0, color='black', linestyle='-', linewidth=0.8)

# 유의성 표시 추가
for i, (idx, row) in enumerate(df_ttest_plot.iterrows()):
    x_pos = row['변화량']
    offset = 0.02 if x_pos > 0 else -0.02
    ha = 'left' if x_pos > 0 else 'right'
    ax.text(x_pos + offset, i, row['유의성'], 
            va='center', ha=ha, fontsize=10, fontweight='bold')

ax.set_xlabel('평균 변화량 (2025 - 2024)', fontsize=12, fontweight='bold')
ax.set_ylabel('역량', fontsize=12, fontweight='bold')
ax.set_title('역량별 연간 평균 변화량 및 통계적 유의성\n(타인평가 기준, 2024 vs 2025)', 
             fontsize=14, fontweight='bold', pad=20)

# 범례 추가
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#d62728', label='p < 0.001 (***)'),
    Patch(facecolor='#ff7f0e', label='p < 0.01 (**)'),
    Patch(facecolor='#2ca02c', label='p < 0.05 (*)'),
    Patch(facecolor='#7f7f7f', label='유의하지 않음 (ns)')
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=10)

ax.grid(axis='x', alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('competency_change_ttest.png', dpi=300, bbox_inches='tight')
plt.show()

# =============================================================================
# 시각화 2: 2024 vs 2025 평균 비교 (유의한 역량만)
# =============================================================================

df_sig = df_ttest[df_ttest['p값'] < 0.05].sort_values('변화량', ascending=False)

if len(df_sig) > 0:
    fig, ax = plt.subplots(figsize=(12, max(6, len(df_sig)*0.4)))
    
    x = np.arange(len(df_sig))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, df_sig['2024_평균'], width, label='2024년', 
                   color='#1f77b4', alpha=0.8)
    bars2 = ax.bar(x + width/2, df_sig['2025_평균'], width, label='2025년', 
                   color='#ff7f0e', alpha=0.8)
    
    # 에러바 추가
    ax.errorbar(x - width/2, df_sig['2024_평균'], yerr=df_sig['2024_표준편차'], 
                fmt='none', ecolor='black', capsize=3, alpha=0.5)
    ax.errorbar(x + width/2, df_sig['2025_평균'], yerr=df_sig['2025_표준편차'], 
                fmt='none', ecolor='black', capsize=3, alpha=0.5)
    
    ax.set_xlabel('역량', fontsize=12, fontweight='bold')
    ax.set_ylabel('평균 점수', fontsize=12, fontweight='bold')
    ax.set_title('통계적으로 유의한 변화를 보인 역량 비교\n(2024 vs 2025, 타인평가)', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(df_sig['역량'], rotation=45, ha='right')
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.savefig('significant_competency_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()
else:
    print("\n유의한 변화를 보인 역량이 없습니다.")

# =============================================================================
# 시각화 3: 효과크기(Cohen's d) 시각화
# =============================================================================

fig, ax = plt.subplots(figsize=(14, 10))

df_ttest_effect = df_ttest.sort_values("Cohen's d", ascending=True).reset_index(drop=True)

# 효과크기 기준 색상
colors_effect = []
for d in df_ttest_effect["Cohen's d"]:
    if abs(d) >= 0.8:
        colors_effect.append('#d62728')  # 큰 효과
    elif abs(d) >= 0.5:
        colors_effect.append('#ff7f0e')  # 중간 효과
    elif abs(d) >= 0.2:
        colors_effect.append('#2ca02c')  # 작은 효과
    else:
        colors_effect.append('#7f7f7f')  # 미미한 효과

bars = ax.barh(df_ttest_effect['역량'], df_ttest_effect["Cohen's d"], 
               color=colors_effect, alpha=0.8)

ax.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
ax.axvline(x=0.2, color='green', linestyle='--', linewidth=0.8, alpha=0.5)
ax.axvline(x=-0.2, color='green', linestyle='--', linewidth=0.8, alpha=0.5)
ax.axvline(x=0.5, color='orange', linestyle='--', linewidth=0.8, alpha=0.5)
ax.axvline(x=-0.5, color='orange', linestyle='--', linewidth=0.8, alpha=0.5)
ax.axvline(x=0.8, color='red', linestyle='--', linewidth=0.8, alpha=0.5)
ax.axvline(x=-0.8, color='red', linestyle='--', linewidth=0.8, alpha=0.5)

ax.set_xlabel("Cohen's d (효과크기)", fontsize=12, fontweight='bold')
ax.set_ylabel('역량', fontsize=12, fontweight='bold')
ax.set_title("역량별 효과크기 (Cohen's d)\n(2024 vs 2025, 타인평가)", 
             fontsize=14, fontweight='bold', pad=20)

# 범례
legend_elements = [
    Patch(facecolor='#d62728', label='큰 효과 (|d| ≥ 0.8)'),
    Patch(facecolor='#ff7f0e', label='중간 효과 (0.5 ≤ |d| < 0.8)'),
    Patch(facecolor='#2ca02c', label='작은 효과 (0.2 ≤ |d| < 0.5)'),
    Patch(facecolor='#7f7f7f', label='미미한 효과 (|d| < 0.2)')
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=10)

ax.grid(axis='x', alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('competency_effect_size.png', dpi=300, bbox_inches='tight')
plt.show()

# =============================================================================
# 결과 저장
# =============================================================================

# Excel로 저장
df_ttest_sorted.to_excel('competency_ttest_results.xlsx', index=False)
print(f"\n결과가 'competency_ttest_results.xlsx' 파일로 저장되었습니다.")
```

### Extracted Code (python)

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
# plt.rcParams['font.family'] = 'AppleGothic'  # Mac
plt.rcParams['axes.unicode_minus'] = False

# =============================================================================
# 분석: 4대 조직별 연간 평균차이 t-test
# =============================================================================

# 분석 대상 조직
TARGET_ORGS = ['PRI 장비기술센터', 'PRI 제조S&P센터', '생산혁신센터', 'PRI 선행공법연구센터']

print("\n" + "="*100)
print("=== 4대 조직별 연간 평균차이 검증 (Independent t-test) ===")
print("="*100)

# 조직별 데이터 필터링 및 검증
org_overall_results = []
org_competency_results = []

for org in TARGET_ORGS:
    print(f"\n{'='*100}")
    print(f"조직: {org}")
    print(f"{'='*100}")
    
    # 해당 조직의 타인평가 데이터만 추출
    df_org_2024 = df2[(df2['년도'] == 2024) & 
                       (df2['구분'] == '타인평가') & 
                       (df2['사업부/담당'] == org)].copy()
    
    df_org_2025 = df2[(df2['년도'] == 2025) & 
                       (df2['구분'] == '타인평가') & 
                       (df2['사업부/담당'] == org)].copy()
    
    print(f"2024년 데이터: {len(df_org_2024)}개")
    print(f"2025년 데이터: {len(df_org_2025)}개")
    
    if len(df_org_2024) == 0 or len(df_org_2025) == 0:
        print(f"⚠️ {org}: 데이터 부족으로 분석 불가")
        continue
    
    # -------------------------------------------------------------------------
    # 1. 전체 평균 비교 (17개 역량 전체)
    # -------------------------------------------------------------------------
    
    # 각 연도별 전체 역량 평균 계산 (개인별)
    overall_2024 = df_org_2024[COMPETENCY_LIST].mean(axis=1).dropna()
    overall_2025 = df_org_2025[COMPETENCY_LIST].mean(axis=1).dropna()
    
    # t-test 수행
    t_stat_overall, p_value_overall = stats.ttest_ind(overall_2025, overall_2024)
    
    # 통계량 계산
    mean_2024_overall = overall_2024.mean()
    mean_2025_overall = overall_2025.mean()
    std_2024_overall = overall_2024.std()
    std_2025_overall = overall_2025.std()
    change_overall = mean_2025_overall - mean_2024_overall
    
    # Cohen's d
    pooled_std_overall = np.sqrt(((len(overall_2024)-1)*std_2024_overall**2 + 
                                   (len(overall_2025)-1)*std_2025_overall**2) / 
                                  (len(overall_2024) + len(overall_2025) - 2))
    cohens_d_overall = change_overall / pooled_std_overall if pooled_std_overall != 0 else 0
    
    # 유의성
    if p_value_overall < 0.001:
        sig_overall = '***'
    elif p_value_overall < 0.01:
        sig_overall = '**'
    elif p_value_overall < 0.05:
        sig_overall = '*'
    else:
        sig_overall = 'ns'
    
    org_overall_results.append({
        '조직': org,
        '2024_평균': mean_2024_overall,
        '2024_표준편차': std_2024_overall,
        '2024_N': len(overall_2024),
        '2025_평균': mean_2025_overall,
        '2025_표준편차': std_2025_overall,
        '2025_N': len(overall_2025),
        '변화량': change_overall,
        't값': t_stat_overall,
        'p값': p_value_overall,
        "Cohen's d": cohens_d_overall,
        '유의성': sig_overall
    })
    
    print(f"\n[전체 역량 평균]")
    print(f"  2024년: {mean_2024_overall:.3f} (±{std_2024_overall:.3f})")
    print(f"  2025년: {mean_2025_overall:.3f} (±{std_2025_overall:.3f})")
    print(f"  변화량: {change_overall:.3f}")
    print(f"  t값: {t_stat_overall:.3f}, p값: {p_value_overall:.6f} {sig_overall}")
    print(f"  Cohen's d: {cohens_d_overall:.3f}")
    
    # -------------------------------------------------------------------------
    # 2. 17개 역량별 비교
    # -------------------------------------------------------------------------
    
    print(f"\n[역량별 상세 분석]")
    print(f"{'역량':<15} {'2024평균':>8} {'2025평균':>8} {'변화량':>8} {'t값':>8} {'p값':>10} {'효과크기':>8} {'유의성':>6}")
    print("-"*90)
    
    for comp in COMPETENCY_LIST:
        # 역량별 데이터 추출
        scores_2024 = df_org_2024[comp].dropna()
        scores_2025 = df_org_2025[comp].dropna()
        
        if len(scores_2024) < 2 or len(scores_2025) < 2:
            continue
        
        # t-test 수행
        t_stat, p_value = stats.ttest_ind(scores_2025, scores_2024)
        
        # 통계량
        mean_2024 = scores_2024.mean()
        mean_2025 = scores_2025.mean()
        std_2024 = scores_2024.std()
        std_2025 = scores_2025.std()
        change = mean_2025 - mean_2024
        
        # Cohen's d
        pooled_std = np.sqrt(((len(scores_2024)-1)*std_2024**2 + 
                              (len(scores_2025)-1)*std_2025**2) / 
                             (len(scores_2024) + len(scores_2025) - 2))
        cohens_d = change / pooled_std if pooled_std != 0 else 0
        
        # 유의성
        if p_value < 0.001:
            significance = '***'
        elif p_value < 0.01:
            significance = '**'
        elif p_value < 0.05:
            significance = '*'
        else:
            significance = 'ns'
        
        org_competency_results.append({
            '조직': org,
            '역량': comp,
            '2024_평균': mean_2024,
            '2024_표준편차': std_2024,
            '2024_N': len(scores_2024),
            '2025_평균': mean_2025,
            '2025_표준편차': std_2025,
            '2025_N': len(scores_2025),
            '변화량': change,
            't값': t_stat,
            'p값': p_value,
            "Cohen's d": cohens_d,
            '유의성': significance
        })
        
        print(f"{comp:<15} {mean_2024:>8.3f} {mean_2025:>8.3f} "
              f"{change:>8.3f} {t_stat:>8.3f} {p_value:>10.6f} "
              f"{cohens_d:>8.3f} {significance:>6}")

# DataFrame 생성
df_org_overall = pd.DataFrame(org_overall_results)
df_org_comp = pd.DataFrame(org_competency_results)

# =============================================================================
# 시각화 1: 조직별 전체 평균 변화 비교
# =============================================================================

if len(df_org_overall) > 0:
    fig, ax = plt.subplots(figsize=(12, 6))
    
    x = np.arange(len(df_org_overall))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, df_org_overall['2024_평균'], width, 
                   label='2024년', color='#1f77b4', alpha=0.8)
    bars2 = ax.bar(x + width/2, df_org_overall['2025_평균'], width, 
                   label='2025년', color='#ff7f0e', alpha=0.8)
    
    # 에러바
    ax.errorbar(x - width/2, df_org_overall['2024_평균'], 
                yerr=df_org_overall['2024_표준편차'], 
                fmt='none', ecolor='black', capsize=5, alpha=0.6)
    ax.errorbar(x + width/2, df_org_overall['2025_평균'], 
                yerr=df_org_overall['2025_표준편차'], 
                fmt='none', ecolor='black', capsize=5, alpha=0.6)
    
    # 유의성 표시
    for i, row in df_org_overall.iterrows():
        y_max = max(row['2024_평균'] + row['2024_표준편차'], 
                    row['2025_평균'] + row['2025_표준편차'])
        ax.text(i, y_max + 0.1, row['유의성'], 
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    ax.set_xlabel('조직', fontsize=12, fontweight='bold')
    ax.set_ylabel('전체 역량 평균 점수', fontsize=12, fontweight='bold')
    ax.set_title('조직별 전체 역량 평균 변화 (2024 vs 2025)\n타인평가 기준', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(df_org_overall['조직'], rotation=15, ha='right')
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_ylim(bottom=0)
    
    plt.tight_layout()
    plt.savefig('org_overall_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

# =============================================================================
# 시각화 2: 조직별 변화량 히트맵
# =============================================================================

if len(df_org_comp) > 0:
    # 피벗 테이블 생성 (조직 x 역량)
    pivot_change = df_org_comp.pivot(index='조직', columns='역량', values='변화량')
    pivot_pvalue = df_org_comp.pivot(index='조직', columns='역량', values='p값')
    
    # 히트맵 그리기
    fig, ax = plt.subplots(figsize=(18, 6))
    
    # 변화량 히트맵
    sns.heatmap(pivot_change, annot=True, fmt='.2f', cmap='RdYlGn', 
                center=0, cbar_kws={'label': '변화량'}, 
                linewidths=0.5, ax=ax)
    
    # 유의한 셀에 표시 추가
    for i in range(len(pivot_change.index)):
        for j in range(len(pivot_change.columns)):
            p_val = pivot_pvalue.iloc[i, j]
            if pd.notna(p_val) and p_val < 0.05:
                ax.add_patch(plt.Rectangle((j, i), 1, 1, 
                                          fill=False, edgecolor='blue', 
                                          lw=3))
    
    ax.set_xlabel('역량', fontsize=12, fontweight='bold')
    ax.set_ylabel('조직', fontsize=12, fontweight='bold')
    ax.set_title('조직별 역량 변화량 히트맵 (2025-2024)\n파란 테두리: p<0.05', 
                 fontsize=14, fontweight='bold', pad=20)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    
    plt.tight_layout()
    plt.savefig('org_competency_heatmap.png', dpi=300, bbox_inches='tight')
    plt.show()

# =============================================================================
# 시각화 3: 조직별 유의한 역량 변화 막대그래프
# =============================================================================

# 유의한 변화만 추출
df_org_sig = df_org_comp[df_org_comp['p값'] < 0.05].copy()

if len(df_org_sig) > 0:
    # 조직별로 서브플롯 생성
    n_orgs = len(TARGET_ORGS)
    fig, axes = plt.subplots(n_orgs, 1, figsize=(14, 4*n_orgs))
    
    if n_orgs == 1:
        axes = [axes]
    
    for idx, org in enumerate(TARGET_ORGS):
        ax = axes[idx]
        df_org_sig_subset = df_org_sig[df_org_sig['조직'] == org].sort_values('변화량', ascending=False)
        
        if len(df_org_sig_subset) > 0:
            # 색상 설정
            colors = ['#d62728' if x < 0 else '#2ca02c' for x in df_org_sig_subset['변화량']]
            
            ax.barh(df_org_sig_subset['역량'], df_org_sig_subset['변화량'], 
                   color=colors, alpha=0.7)
            ax.axvline(x=0, color='black', linestyle='-', linewidth=1)
            
            # 유의성 표시
            for i, (_, row) in enumerate(df_org_sig_subset.iterrows()):
                x_pos = row['변화량']
                offset = 0.03 if x_pos > 0 else -0.03
                ha = 'left' if x_pos > 0 else 'right'
                ax.text(x_pos + offset, i, row['유의성'], 
                       va='center', ha=ha, fontsize=10, fontweight='bold')
            
            ax.set_xlabel('변화량', fontsize=11, fontweight='bold')
            ax.set_title(f'{org} - 유의한 역량 변화 (p<0.05)', 
                        fontsize=12, fontweight='bold')
            ax.grid(axis='x', alpha=0.3, linestyle='--')
        else:
            ax.text(0.5, 0.5, f'{org}\n유의한 변화 없음', 
                   ha='center', va='center', fontsize=12, 
                   transform=ax.transAxes)
            ax.set_xticks([])
            ax.set_yticks([])
    
    plt.tight_layout()
    plt.savefig('org_significant_changes.png', dpi=300, bbox_inches='tight')
    plt.show()
else:
    print("\n⚠️ 유의한 변화를 보인 역량이 없습니다.")

# =============================================================================
# 시각화 4: 조직별 효과크기 비교
# =============================================================================

if len(df_org_comp) > 0:
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # 조직별로 색상 구분
    org_colors = {'PRI 장비기술센터': '#1f77b4', 
                  'PRI 제조S&P센터': '#ff7f0e',
                  '생산혁신센터': '#2ca02c',
                  'PRI 선행공법연구센터': '#d62728'}
    
    for org in TARGET_ORGS:
        df_temp = df_org_comp[df_org_comp['조직'] == org].sort_values('역량')
        if len(df_temp) > 0:
            ax.scatter(df_temp['역량'], df_temp["Cohen's d"], 
                      label=org, s=100, alpha=0.7, 
                      color=org_colors.get(org, '#7f7f7f'))
    
    # 효과크기 기준선
    ax.axhline(y=0, color='black', linestyle='-', linewidth=1)
    ax.axhline(y=0.2, color='green', linestyle='--', linewidth=0.8, alpha=0.5)
    ax.axhline(y=-0.2, color='green', linestyle='--', linewidth=0.8, alpha=0.5)
    ax.axhline(y=0.5, color='orange', linestyle='--', linewidth=0.8, alpha=0.5)
    ax.axhline(y=-0.5, color='orange', linestyle='--', linewidth=0.8, alpha=0.5)
    ax.axhline(y=0.8, color='red', linestyle='--', linewidth=0.8, alpha=0.5)
    ax.axhline(y=-0.8, color='red', linestyle='--', linewidth=0.8, alpha=0.5)
    
    ax.set_xlabel('역량', fontsize=12, fontweight='bold')
    ax.set_ylabel("Cohen's d (효과크기)", fontsize=12, fontweight='bold')
    ax.set_title("조직별 역량 변화 효과크기 비교\n(2024 vs 2025, 타인평가)", 
                fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='best', fontsize=10)
    ax.grid(alpha=0.3, linestyle='--')
    plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    plt.savefig('org_effect_size_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

# =============================================================================
# 결과 요약 출력
# =============================================================================

print("\n" + "="*100)
print("=== 조직별 전체 평균 검증 결과 요약 ===")
print("="*100)
if len(df_org_overall) > 0:
    print(df_org_overall[['조직', '2024_평균', '2025_평균', '변화량', 
                           't값', 'p값', "Cohen's d", '유의성']].to_string(index=False))

print("\n" + "="*100)
print("=== 조직별 유의한 역량 변화 요약 ===")
print("="*100)
for org in TARGET_ORGS:
    sig_comps = df_org_comp[(df_org_comp['조직'] == org) & (df_org_comp['p값'] < 0.05)]
    if len(sig_comps) > 0:
        print(f"\n{org}: {len(sig_comps)}개 역량에서 유의한 변화")
        for _, row in sig_comps.iterrows():
            direction = "증가" if row['변화량'] > 0 else "감소"
            print(f"  - {row['역량']}: {row['변화량']:.3f} ({direction}) {row['유의성']}")
    else:
        print(f"\n{org}: 유의한 변화 없음")

# =============================================================================
# 결과 저장
# =============================================================================

with pd.ExcelWriter('org_ttest_results.xlsx') as writer:
    df_org_overall.to_excel(writer, sheet_name='조직별_전체평균', index=False)
    df_org_comp.to_excel(writer, sheet_name='조직별_역량별', index=False)
    
    # 유의한 결과만 별도 시트
    if len(df_org_sig) > 0:
        df_org_sig.to_excel(writer, sheet_name='유의한_변화', index=False)

print(f"\n✅ 결과가 'org_ttest_results.xlsx' 파일로 저장되었습니다.")
print(f"✅ 4개의 시각화 파일이 저장되었습니다:")
print(f"   - org_overall_comparison.png")
print(f"   - org_competency_heatmap.png")
print(f"   - org_significant_changes.png")
print(f"   - org_effect_size_comparison.png")
```

### Extracted Code (python)

```python
import nbformat

# 노트북 파일 읽기
with open('/mnt/user-data/uploads/리더십평가_고과평균_회귀분석.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# 노트북 구조 확인
print(f"총 셀 개수: {len(nb.cells)}")
print("\n=== 노트북 구조 ===")
for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'markdown':
        # 마크다운 셀의 첫 줄만 출력
        first_line = cell.source.split('\n')[0][:50]
        print(f"Cell {i}: [Markdown] {first_line}")
    elif cell.cell_type == 'code':
        # 코드 셀의 첫 줄만 출력
        first_line = cell.source.split('\n')[0][:50] if cell.source else "(empty)"
        print(f"Cell {i}: [Code] {first_line}")
```

### Extracted Code (markdown)

```markdown
---
# 분석 5: 조직별 연간 평균차이 검증 (t-test)

## 목적
- 4대 조직별 2024년 vs 2025년 타인평가 평균 차이 검증
- 조직별 전체 역량 평균 및 17개 역량별 변화 분석
- 통계적 유의성 및 효과크기 측정
```

### Extracted Code (python)

```python
# =============================================================================
# 분석 6: 25년 4대 조직의 평가구분별 평가결과 분석
# =============================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
# plt.rcParams['font.family'] = 'AppleGothic'  # Mac
plt.rcParams['axes.unicode_minus'] = False

# 4대 조직 정의
TARGET_ORGS = ['PRI 장비기술센터', 'PRI 제조S&P센터', '생산혁신센터', 'PRI 선행공법연구센터']

# 평가구분 정의 (df2의 '구분' 컬럼에 있는 값들)
EVAL_TYPES = ['본인평가', '타인평가', '상사', '동료', '구성원']

print("="*100)
print("=== 25년 4대 조직의 평가구분별 평가결과 분석 ===")
print("="*100)

# 2025년 데이터만 필터링
df_2025 = df2[df2['년도'] == 2025].copy()

print(f"\n2025년 전체 데이터: {len(df_2025)}개")

# =============================================================================
# 1. 조직별 평가구분별 데이터 개수 확인
# =============================================================================

print("\n" + "="*100)
print("=== 조직별 평가구분별 데이터 현황 ===")
print("="*100)

data_count_summary = []

for org in TARGET_ORGS:
    print(f"\n[{org}]")
    df_org = df_2025[df_2025['사업부/담당'] == org]
    
    for eval_type in EVAL_TYPES:
        count = len(df_org[df_org['구분'] == eval_type])
        data_count_summary.append({
            '조직': org,
            '평가구분': eval_type,
            '데이터수': count
        })
        print(f"  {eval_type}: {count}개")

df_data_count = pd.DataFrame(data_count_summary)

# =============================================================================
# 2. 조직별 평가구분별 전체 역량 평균 계산
# =============================================================================

print("\n" + "="*100)
print("=== 조직별 평가구분별 전체 역량 평균 ===")
print("="*100)

org_eval_results = []

for org in TARGET_ORGS:
    print(f"\n[{org}]")
    df_org = df_2025[df_2025['사업부/담당'] == org]
    
    for eval_type in EVAL_TYPES:
        df_eval = df_org[df_org['구분'] == eval_type]
        
        if len(df_eval) == 0:
            continue
        
        # 전체 역량 평균 (17개 역량)
        overall_scores = df_eval[COMPETENCY_LIST].mean(axis=1).dropna()
        
        if len(overall_scores) > 0:
            mean_score = overall_scores.mean()
            std_score = overall_scores.std()
            
            org_eval_results.append({
                '조직': org,
                '평가구분': eval_type,
                '평균': mean_score,
                '표준편차': std_score,
                'N': len(overall_scores)
            })
            
            print(f"  {eval_type}: {mean_score:.3f} (±{std_score:.3f}), N={len(overall_scores)}")

df_org_eval = pd.DataFrame(org_eval_results)

# =============================================================================
# 3. 조직별 평가구분별 17개 역량 상세 분석
# =============================================================================

print("\n" + "="*100)
print("=== 조직별 평가구분별 역량별 평균 ===")
print("="*100)

org_eval_comp_results = []

for org in TARGET_ORGS:
    print(f"\n{'='*100}")
    print(f"[{org}]")
    print(f"{'='*100}")
    
    df_org = df_2025[df_2025['사업부/담당'] == org]
    
    for eval_type in EVAL_TYPES:
        df_eval = df_org[df_org['구분'] == eval_type]
        
        if len(df_eval) == 0:
            continue
        
        print(f"\n--- {eval_type} ---")
        print(f"{'역량':<15} {'평균':>8} {'표준편차':>8} {'N':>6}")
        print("-"*45)
        
        for comp in COMPETENCY_LIST:
            scores = df_eval[comp].dropna()
            
            if len(scores) > 0:
                mean_score = scores.mean()
                std_score = scores.std()
                
                org_eval_comp_results.append({
                    '조직': org,
                    '평가구분': eval_type,
                    '역량': comp,
                    '평균': mean_score,
                    '표준편차': std_score,
                    'N': len(scores)
                })
                
                print(f"{comp:<15} {mean_score:>8.3f} {std_score:>8.3f} {len(scores):>6}")

df_org_eval_comp = pd.DataFrame(org_eval_comp_results)

# =============================================================================
# 시각화 1: 조직별 평가구분별 전체 평균 비교
# =============================================================================

if len(df_org_eval) > 0:
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    axes = axes.flatten()
    
    for idx, org in enumerate(TARGET_ORGS):
        ax = axes[idx]
        df_org_subset = df_org_eval[df_org_eval['조직'] == org]
        
        if len(df_org_subset) > 0:
            x = np.arange(len(df_org_subset))
            bars = ax.bar(x, df_org_subset['평균'], 
                         color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'][:len(df_org_subset)],
                         alpha=0.8)
            
            # 에러바
            ax.errorbar(x, df_org_subset['평균'], 
                       yerr=df_org_subset['표준편차'],
                       fmt='none', ecolor='black', capsize=5, alpha=0.6)
            
            # 값 표시
            for i, (bar, val) in enumerate(zip(bars, df_org_subset['평균'])):
                ax.text(bar.get_x() + bar.get_width()/2, val + 0.05,
                       f'{val:.2f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
            
            ax.set_xticks(x)
            ax.set_xticklabels(df_org_subset['평가구분'], rotation=15, ha='right')
            ax.set_ylabel('전체 역량 평균', fontsize=11, fontweight='bold')
            ax.set_title(f'{org}', fontsize=12, fontweight='bold')
            ax.grid(axis='y', alpha=0.3, linestyle='--')
            ax.set_ylim(bottom=0)
        else:
            ax.text(0.5, 0.5, f'{org}\n데이터 없음', 
                   ha='center', va='center', fontsize=12, transform=ax.transAxes)
            ax.set_xticks([])
            ax.set_yticks([])
    
    plt.suptitle('조직별 평가구분별 전체 역량 평균 비교 (2025년)', 
                 fontsize=14, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.show()

# =============================================================================
# 시각화 2: 평가구분별 조직 비교 (전체 평균)
# =============================================================================

if len(df_org_eval) > 0:
    # 피벗 테이블 생성
    pivot_org_eval = df_org_eval.pivot(index='조직', columns='평가구분', values='평균')
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    x = np.arange(len(TARGET_ORGS))
    width = 0.15
    
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    eval_types_available = [col for col in EVAL_TYPES if col in pivot_org_eval.columns]
    
    for i, eval_type in enumerate(eval_types_available):
        offset = width * (i - len(eval_types_available)/2 + 0.5)
        values = [pivot_org_eval.loc[org, eval_type] if org in pivot_org_eval.index and pd.notna(pivot_org_eval.loc[org, eval_type]) else 0 
                  for org in TARGET_ORGS]
        ax.bar(x + offset, values, width, label=eval_type, color=colors[i], alpha=0.8)
    
    ax.set_xlabel('조직', fontsize=12, fontweight='bold')
    ax.set_ylabel('전체 역량 평균', fontsize=12, fontweight='bold')
    ax.set_title('평가구분별 조직 비교 (2025년)', fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(TARGET_ORGS, rotation=15, ha='right')
    ax.legend(title='평가구분', fontsize=10)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.show()

# =============================================================================
# 시각화 3: 조직별 역량×평가구분 히트맵
# =============================================================================

if len(df_org_eval_comp) > 0:
    for org in TARGET_ORGS:
        df_org_comp_subset = df_org_eval_comp[df_org_eval_comp['조직'] == org]
        
        if len(df_org_comp_subset) > 0:
            # 피벗 테이블 생성 (역량 x 평가구분)
            pivot_comp_eval = df_org_comp_subset.pivot(index='역량', columns='평가구분', values='평균')
            
            fig, ax = plt.subplots(figsize=(10, 12))
            
            sns.heatmap(pivot_comp_eval, annot=True, fmt='.2f', cmap='YlOrRd',
                       linewidths=0.5, cbar_kws={'label': '평균 점수'}, ax=ax)
            
            ax.set_xlabel('평가구분', fontsize=12, fontweight='bold')
            ax.set_ylabel('역량', fontsize=12, fontweight='bold')
            ax.set_title(f'{org} - 역량별 평가구분 비교 (2025년)', 
                        fontsize=14, fontweight='bold', pad=20)
            plt.xticks(rotation=45, ha='right')
            plt.yticks(rotation=0)
            
            plt.tight_layout()
            plt.show()

# =============================================================================
# 시각화 4: 평가구분 간 차이 분석 (본인평가 vs 타인평가)
# =============================================================================

if len(df_org_eval) > 0:
    # 본인평가와 타인평가가 모두 있는 조직만 필터링
    eval_comparison = []
    
    for org in TARGET_ORGS:
        df_org_subset = df_org_eval[df_org_eval['조직'] == org]
        
        self_eval = df_org_subset[df_org_subset['평가구분'] == '본인평가']
        other_eval = df_org_subset[df_org_subset['평가구분'] == '타인평가']
        
        if len(self_eval) > 0 and len(other_eval) > 0:
            self_score = self_eval['평균'].values[0]
            other_score = other_eval['평균'].values[0]
            diff = self_score - other_score
            
            eval_comparison.append({
                '조직': org,
                '본인평가': self_score,
                '타인평가': other_score,
                '차이(본인-타인)': diff
            })
    
    if len(eval_comparison) > 0:
        df_eval_comp = pd.DataFrame(eval_comparison)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        x = np.arange(len(df_eval_comp))
        width = 0.35
        
        bars1 = ax.bar(x - width/2, df_eval_comp['본인평가'], width,
                      label='본인평가', color='#1f77b4', alpha=0.8)
        bars2 = ax.bar(x + width/2, df_eval_comp['타인평가'], width,
                      label='타인평가', color='#ff7f0e', alpha=0.8)
        
        # 차이 표시
        for i, row in df_eval_comp.iterrows():
            y_pos = max(row['본인평가'], row['타인평가']) + 0.1
            diff_text = f"차이: {row['차이(본인-타인)']:+.2f}"
            color = 'red' if row['차이(본인-타인)'] > 0 else 'blue'
            ax.text(i, y_pos, diff_text, ha='center', va='bottom',
                   fontsize=10, fontweight='bold', color=color)
        
        ax.set_xlabel('조직', fontsize=12, fontweight='bold')
        ax.set_ylabel('전체 역량 평균', fontsize=12, fontweight='bold')
        ax.set_title('본인평가 vs 타인평가 비교 (2025년)', 
                    fontsize=14, fontweight='bold', pad=20)
        ax.set_xticks(x)
        ax.set_xticklabels(df_eval_comp['조직'], rotation=15, ha='right')
        ax.legend(fontsize=11)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        plt.tight_layout()
        plt.show()
        
        print("\n" + "="*100)
        print("=== 본인평가 vs 타인평가 차이 ===")
        print("="*100)
        print(df_eval_comp.to_string(index=False))

# =============================================================================
# 시각화 5: 평가자 유형별 비교 (상사, 동료, 구성원)
# =============================================================================

if len(df_org_eval) > 0:
    # 상사, 동료, 구성원 평가가 있는 조직 필터링
    rater_comparison = []
    
    for org in TARGET_ORGS:
        df_org_subset = df_org_eval[df_org_eval['조직'] == org]
        
        for rater_type in ['상사', '동료', '구성원']:
            rater_eval = df_org_subset[df_org_subset['평가구분'] == rater_type]
            
            if len(rater_eval) > 0:
                rater_comparison.append({
                    '조직': org,
                    '평가자유형': rater_type,
                    '평균': rater_eval['평균'].values[0]
                })
    
    if len(rater_comparison) > 0:
        df_rater_comp = pd.DataFrame(rater_comparison)
        
        fig, ax = plt.subplots(figsize=(14, 6))
        
        # 평가자 유형별 색상
        rater_colors = {'상사': '#2ca02c', '동료': '#d62728', '구성원': '#9467bd'}
        
        for rater_type in ['상사', '동료', '구성원']:
            df_rater = df_rater_comp[df_rater_comp['평가자유형'] == rater_type]
            
            if len(df_rater) > 0:
                orgs = df_rater['조직'].values
                scores = df_rater['평균'].values
                x_pos = [TARGET_ORGS.index(org) for org in orgs]
                
                ax.plot(x_pos, scores, marker='o', linewidth=2, markersize=10,
                       label=rater_type, color=rater_colors.get(rater_type, 'gray'), alpha=0.8)
                
                # 값 표시
                for x, y in zip(x_pos, scores):
                    ax.text(x, y + 0.05, f'{y:.2f}', ha='center', va='bottom',
                           fontsize=9, fontweight='bold')
        
        ax.set_xlabel('조직', fontsize=12, fontweight='bold')
        ax.set_ylabel('전체 역량 평균', fontsize=12, fontweight='bold')
        ax.set_title('평가자 유형별 조직 비교 (2025년)', 
                    fontsize=14, fontweight='bold', pad=20)
        ax.set_xticks(range(len(TARGET_ORGS)))
        ax.set_xticklabels(TARGET_ORGS, rotation=15, ha='right')
        ax.legend(title='평가자 유형', fontsize=11)
        ax.grid(alpha=0.3, linestyle='--')
        
        plt.tight_layout()
        plt.show()

# =============================================================================
# 결과 저장
# =============================================================================

with pd.ExcelWriter('25년_조직별_평가구분_분석.xlsx') as writer:
    df_data_count.to_excel(writer, sheet_name='데이터현황', index=False)
    df_org_eval.to_excel(writer, sheet_name='조직별_평가구분별_전체평균', index=False)
    df_org_eval_comp.to_excel(writer, sheet_name='조직별_평가구분별_역량별', index=False)

print("\n✅ 결과가 '25년_조직별_평가구분_분석.xlsx' 파일로 저장되었습니다.")
print("\n분석 완료!")
```
