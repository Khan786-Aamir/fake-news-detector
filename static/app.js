// static/app.js
document.addEventListener("DOMContentLoaded", () => {
  const newsInput = document.getElementById("newsInput");
  const predictBtn = document.getElementById("predictBtn");
  const resultDiv = document.getElementById("result");

  // Helper function: show styled result
  function showResult(message, type) {
    resultDiv.style.display = "block";
    resultDiv.classList.remove("success", "error");
    if (type === "success") resultDiv.classList.add("success");
    if (type === "error") resultDiv.classList.add("error");
    resultDiv.innerHTML = message;
  }

  async function predictFakeNews() {
    const newsText = newsInput.value.trim();

    if (!newsText) {
      showResult("⚠️ Pehle news likho!", "error");
      return;
    }

    showResult("⏳ Analyzing news...", "info");
    predictBtn.disabled = true;
    const oldText = predictBtn.innerHTML;
    predictBtn.innerHTML = "Analyzing...";

    try {
      const response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: newsText }),
      });

      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }

      const data = await response.json();

      let labelText;
      if (data.label === 1 || data.label === "FAKE") {
        labelText = "❌ This news is <strong>Fake</strong>!";
        showResult(labelText, "error");
      } else if (data.label === 0 || data.label === "REAL") {
        labelText = "✅ This news is <strong>Real</strong>!";
        showResult(labelText, "success");
      } else {
        labelText = "⚠️ Could not determine the prediction.";
        showResult(labelText, "error");
      }

      // Confidence/probability
      if (data.probability !== undefined && data.probability !== null) {
        const conf = (data.probability * 100).toFixed(1);
        resultDiv.innerHTML += `<br/><small>Confidence: ${conf}%</small>`;
      }
    } catch (err) {
      showResult(`⚠️ Error: ${err.message}`, "error");
      console.error(err);
    } finally {
      predictBtn.disabled = false;
      predictBtn.innerHTML = oldText;
    }
  }

  // Button click event
  predictBtn.addEventListener("click", predictFakeNews);

  // Shortcut: Ctrl+Enter for quick submit
  newsInput.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
      predictFakeNews();
    }
  });
});
