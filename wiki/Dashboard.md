# 📊 Wiki Dashboard

Live overview of the OmegaWiki state. Updated dynamically by Dataview.

---

## 🔢 Wiki Stats

```dataview
TABLE WITHOUT ID
  "📄 Papers" as Type, length(rows) as Count
FROM "papers"
GROUP BY "all"
```

```dataview
TABLE WITHOUT ID
  "🧠 Concepts" as Type, length(rows) as Count
FROM "concepts"
GROUP BY "all"
```

```dataview
TABLE WITHOUT ID
  "🏗️ Foundations" as Type, length(rows) as Count
FROM "foundations"
GROUP BY "all"
```

```dataview
TABLE WITHOUT ID
  "💬 Claims" as Type, length(rows) as Count
FROM "claims"
GROUP BY "all"
```

```dataview
TABLE WITHOUT ID
  "👤 People" as Type, length(rows) as Count
FROM "people"
GROUP BY "all"
```

---

## 📚 Papers ranked by connections

```dataview
TABLE 
  importance as "★",
  tier,
  year,
  length(file.outlinks) as "Outlinks",
  length(file.inlinks) as "Inlinks"
FROM "papers"
SORT length(file.outlinks) DESC
```

---

## 🧠 Top 10 most-connected concepts

```dataview
TABLE 
  length(file.inlinks) as "Inlinks",
  maturity
FROM "concepts"
SORT length(file.inlinks) DESC
LIMIT 10
```

---

## 🏗️ Top 10 most-used foundations

```dataview
TABLE 
  length(file.inlinks) as "Used in"
FROM "foundations"
WHERE length(file.inlinks) > 0
SORT length(file.inlinks) DESC
LIMIT 10
```

---

## 👤 People with multiple papers in vault

```dataview
TABLE 
  papers_in_vault as "Papers",
  relevance_tier as "Tier",
  manual_override as "Override"
FROM "people"
WHERE papers_in_vault > 1
SORT papers_in_vault DESC
```

---

## 🎯 Claims by confidence level (top 15)

```dataview
TABLE 
  confidence,
  status,
  type
FROM "claims"
WHERE confidence != null
SORT confidence DESC
LIMIT 15
```

---

## 🩺 Papers by tissue

```dataview
TABLE 
  tissue,
  condition,
  importance as "★"
FROM "papers"
WHERE tissue != null
SORT importance DESC
```

---

## ⚠️ Papers without tissue (data quality check)

```dataview
LIST
FROM "papers"
WHERE tissue = null OR length(tissue) = 0
```

---

## 🆕 Recently added papers

```dataview
TABLE 
  ingested_date as "Ingested",
  importance as "★",
  length(file.outlinks) as "Outlinks"
FROM "papers"
SORT ingested_date DESC
LIMIT 5
```

---

## 🌫️ Hypoxia-relevant papers

```dataview
TABLE 
  tissue,
  importance as "★",
  year
FROM "papers"
WHERE hypoxia_relevant = true
SORT importance DESC
```

---

## 🔬 Skin-relevant papers

```dataview
TABLE 
  tissue,
  importance as "★",
  year
FROM "papers"
WHERE contains(tissue, "skin") OR contains(string(tags), "skin")
```