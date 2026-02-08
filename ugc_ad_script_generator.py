diff --git a/README.md b/README.md
index 236838bf7a73cd6f6e20c4314f845bc53671618b..7112c7c649c66f094fa5f43f216f0edf2a808056 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,16 @@
 # task-2-AI-Content-Marketing-using-UGC-Ads-
 internship project AI Content Marketing using UGC Ads using prompt engineering 
+
+## UGC Ad Script Generator (Random AI Software Product)
+
+Run the script below to generate a fresh 30-second, testimonial-style UGC ad script with:
+- Hook, problem, solution, social proof, and CTA
+- Visual direction notes
+- Text overlay suggestions
+- A caption ready for Reels/Stories
+
+```bash
+python3 ugc_ad_script_generator.py
+```
+
+The generator randomly selects an AI software product and prints a complete script.
diff --git a/ugc_ad_script_generator.py b/ugc_ad_script_generator.py
new file mode 100644
index 0000000000000000000000000000000000000000..38067f0263123c879cbb70c0770dfe994dd08c12
--- /dev/null
+++ b/ugc_ad_script_generator.py
@@ -0,0 +1,135 @@
+#!/usr/bin/env python3
+"""
+UGC Ad Script Generator
+Creates a 30-second, testimonial-style ad script for a random AI software product.
+"""
+
+from __future__ import annotations
+
+import random
+from dataclasses import dataclass
+
+
+@dataclass(frozen=True)
+class Product:
+    name: str
+    category: str
+    benefits: list[str]
+    audience: str
+    usp: str
+
+
+PRODUCTS = [
+    Product(
+        name="ClipGenius AI",
+        category="AI video editing & captioning software",
+        benefits=[
+            "auto-captions in seconds",
+            "removes filler words",
+            "adds trending subtitles",
+            "exports in Reels-ready size",
+            "saves hours per video",
+        ],
+        audience="18–35 creators in the US/UK, overwhelmed by editing time and inconsistent engagement",
+        usp="one-tap “Viral Edit” that applies captions, cuts, and highlight zooms automatically",
+    ),
+    Product(
+        name="InboxSage AI",
+        category="AI email triage & summarization tool",
+        benefits=[
+            "summarizes long threads",
+            "drafts quick replies",
+            "prioritizes urgent messages",
+            "reduces inbox anxiety",
+            "saves 30–60 minutes daily",
+        ],
+        audience="25–45 professionals in North America, drowning in email and missing important tasks",
+        usp="auto-briefs every thread in one swipe with action items",
+    ),
+    Product(
+        name="DeckSpark AI",
+        category="AI slide deck generator",
+        benefits=[
+            "turns outlines into slides",
+            "auto-designs layouts",
+            "adds visuals instantly",
+            "keeps brand colors consistent",
+            "cuts prep time in half",
+        ],
+        audience="22–40 marketers and founders in Europe, under tight deadlines and low design resources",
+        usp="one-click “Pitch Mode” that builds a 10-slide deck from bullet points",
+    ),
+    Product(
+        name="ShopPilot AI",
+        category="AI ecommerce product description writer",
+        benefits=[
+            "writes SEO-ready descriptions",
+            "generates benefit-focused bullets",
+            "matches brand tone",
+            "boosts conversion copy",
+            "publishes in seconds",
+        ],
+        audience="20–45 small business owners in Australia/US, stuck on writing copy and launching late",
+        usp="uploads a product photo and drafts a full listing automatically",
+    ),
+]
+
+
+def build_script(product: Product) -> str:
+    benefits_line = ", ".join(product.benefits)
+    return f"""## UGC Ad Script (Random AI Software Product)
+
+**Product Details (Randomized)**
+- **Product Name:** {product.name}
+- **Category:** {product.category}
+- **Key Benefits:** {benefits_line}
+- **Target Audience:** {product.audience}
+- **Unique Selling Point:** {product.usp}
+
+### 1) Hook line (exact words to say)
+“Okay, I did *not* want to learn this the hard way… but {product.name} made it feel easy in, like, minutes.”
+
+### 2) Full script with timing markers (30s max)
+**0–3s (Hook):**  
+“Okay, I did *not* want to learn this the hard way… but {product.name} made it feel easy in, like, minutes.”  
+
+**3–8s (Problem):**  
+“I kept losing time to the little stuff and honestly I was ready to give up.”  
+
+**8–20s (Solution):**  
+“So I tried {product.name}. I just open it, tap the main action, and it {product.benefits[0]}, {product.benefits[1]}, and {product.benefits[2]}. I’m like, wait… that’s it?”  
+
+**20–25s (Social Proof):**  
+“My results got noticeably better in a week, and friends were like, ‘What are you using?’”  
+
+**25–30s (CTA):**  
+“If you want faster results without the headache, just try {product.name}. I’ll link it.”  
+
+### 3) Visual direction notes
+- **Style:** Selfie-style intro, then quick screen recording/B-roll of the app in action.  
+- **Shots:**  
+  - Hook: front camera, casual setting.  
+  - Problem: quick cut to stressed face or cluttered workspace.  
+  - Solution: screen capture of the main action and the output.  
+  - Social proof: overlay of analytics/DMs (mocked).  
+  - CTA: selfie outro pointing to link sticker.  
+
+### 4) Text overlay suggestions
+- “No time for the busywork? Same.”  
+- “{product.benefits[0].title()}”  
+- “{product.benefits[1].title()}”  
+- “Results in a week”  
+- “Try {product.name} →”  
+
+### 5) Caption for post
+“I was *this close* to quitting 😅 {product.name} saved me hours and made things way easier. Try it if you’re tired of the grind.”  
+"""
+
+
+def main() -> None:
+    product = random.choice(PRODUCTS)
+    print(build_script(product))
+
+
+if __name__ == "__main__":
+    main()
