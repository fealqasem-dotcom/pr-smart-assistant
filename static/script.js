function login() {
  alert("تسجيل الدخول شغال ✅");
}

function logout() {
  alert("تم تسجيل الخروج");
}

function chooseFree() {

  alert(
    "تم تفعيل الباقة المجانية ✅\n\n" +
    "تحصل على 5 استخدامات يومياً"
  );
}

function payNow(plan) {

  const planName =
    plan === "pro"
      ? "AURA Pro"
      : "AURA VIP";

  alert(
    "للاشتراك في " +
    planName +
    "\n\n" +
    "راسلنا عبر الإيميل أو حساب X أسفل الصفحة."
  );
}

function openService(service) {

  const names = {
    summary: "تلخيص النصوص",
    rewrite: "إعادة الصياغة",
    translate: "الترجمة",
    email: "كتابة بريد",
    content: "أفكار محتوى",
    explain: "شرح مبسط"
  };

  const toolBox =
    document.getElementById("toolBox");

  const toolTitle =
    document.getElementById("toolTitle");

  if (!toolBox || !toolTitle) {
    alert("toolBox غير موجود");
    return;
  }

  toolBox.style.display = "block";

  toolTitle.innerText =
    names[service] || service;

  const modeInput =
    document.getElementById("modeInput");

  if (modeInput) {
    modeInput.value = service;
  }

  toolBox.scrollIntoView({
    behavior: "smooth"
  });
}

function keepToolOpen() {

  localStorage.setItem(
    "toolOpen",
    "yes"
  );
}

window.onload = function () {

  const toolOpen =
    localStorage.getItem("toolOpen");

  if (toolOpen === "yes") {

    const toolBox =
      document.getElementById("toolBox");

    if (toolBox) {

      toolBox.style.display = "block";

      toolBox.scrollIntoView({
        behavior: "smooth"
      });
    }

    localStorage.removeItem("toolOpen");
  }
};