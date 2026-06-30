# Extracted Knowledge from Conv: ad0b0513-af4f-4b09-b97c-fffcf99024cf

**Date**: 2025-11-05T23:40:45.917478Z

### Extracted Code (text)

```text
기술 스킬 (Hard Skills)
├─ 프로그래밍
│  ├─ 언어
│  │  ├─ Python
│  │  ├─ Java
│  │  └─ JavaScript
│  └─ 프레임워크
│     ├─ Django
│     └─ Spring
├─ 데이터 분석
│  ├─ SQL
│  ├─ 통계
│  └─ 머신러닝

소프트 스킬 (Soft Skills)
├─ 커뮤니케이션
├─ 리더십
└─ 문제 해결
```

### Extracted Code (text)

```text
Python --requires--> 프로그래밍 기초
Python --enables--> 데이터 분석
Python --similar-to--> R
Django --requires--> Python
풀스택 개발 --combines--> 프론트엔드 + 백엔드
```

### Extracted Code (xml)

```xml
<Skill rdf:about="Python">
  <rdfs:subClassOf rdf:resource="ProgrammingLanguage"/>
  <hasLevel rdf:resource="Beginner"/>
  <requires rdf:resource="ProgrammingFundamentals"/>
</Skill>
```

### Extracted Code (json)

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "Python",
  "inDefinedTermSet": "Programming Languages",
  "requires": ["Programming Fundamentals"],
  "related": ["Data Analysis", "Machine Learning"]
}
```

### Extracted Code (cypher)

```cypher
CREATE (p:Skill {name: 'Python', type: 'Programming'})
CREATE (ml:Skill {name: 'Machine Learning'})
CREATE (p)-[:ENABLES]->(ml)
```
