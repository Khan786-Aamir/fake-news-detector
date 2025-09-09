// static/app.js

async function predictFakeNews() {
  const newsText = document.getElementById("newsInput").value.trim();
  const resultDiv = document.getElementById("result");

  if (!newsText) {
    resultDiv.textContent = "⚠️ Pehle news likho!";
    resultDiv.style.color = "#d00";
    return;
  }

  resultDiv.textContent = "⏳ Predicting...";
  resultDiv.style.color = "#333";

  try {
    const response = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: newsText }),
    });

    if (!response.ok) {
      throw new Error(`Server Error: ${response.status}`);
    }

    const data = await response.json();

    if (data.label === 1) {
      resultDiv.textContent = "❌ This news is Fake!";
      resultDiv.style.color = "#d00";
    } else if (data.label === 0) {
      resultDiv.textContent = "✅ This news is Real!";
      resultDiv.style.color = "#2d8a34";
    } else {
      resultDiv.textContent = "⚠️ Could not determine the prediction.";
      resultDiv.style.color = "#999";
    }

    if (data.probability !== undefined && data.probability !== null) {
      const conf = (data.probability * 100).toFixed(1);
      resultDiv.textContent += ` (Confidence: ${conf}%)`;
    }
  } catch (err) {
    resultDiv.textContent = `⚠️ Error: ${err.message}`;
    resultDiv.style.color = "#d00";
  }
}

// Event listener lagao
document.getElementById("predictBtn").addEventListener("click", predictFakeNews);
