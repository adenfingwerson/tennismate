import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the Service Cards
content = re.sub(
    r'<div class="service-card reveal">.*?</div>\s*</div>\s*<div class="service-add-on reveal">.*?</div>',
    """<div class="service-card reveal" style="width: 100%; max-width: 400px; margin: 0 auto;">
      <div class="service-num">01</div>
      <div class="service-type">Standard Session</div>
      <div class="service-name">1-Hour Lesson</div>
      <p class="service-desc">Complete customized instruction: coaching, hitting drills, match play, or technical adjustments tailored fully to your goals.</p>
      <div class="service-price" style="margin-bottom: 1.5rem;">
        <span class="price-amount">$25</span>
        <span class="price-unit">per hour</span>
      </div>
    </div>
  </div>""",
    content,
    flags=re.DOTALL
)

# 2. Update the Pricing Bar
content = re.sub(
    r'<div class="pricing-bar">.*?</div>\s*</div>',
    """<div class="pricing-bar">
        <div class="price-item" style="width: 100%; border-right: none; justify-content: center;">
          <span>🎾 Single 1-Hour Lesson</span>
          <strong>$25 / hr</strong>
        </div>
      </div>""",
    content,
    count=1,
    flags=re.DOTALL
)

# 3. Update the iframe src
content = content.replace(
    'src="https://calendar.google.com/calendar/appointments/schedules/AcZssZ1aMaYFfS5CqV2J442kfd7Qd_VNECRxVGSW_XQJOGh5tMOrCtPhbN5Ep_k7aBCegbI0wrsis1m2?gv=true"',
    'src="https://tennistmate.setmore.com"'
)
content = content.replace(
    'href="https://calendar.google.com/calendar/appointments/schedules/AcZssZ1aMaYFfS5CqV2J442kfd7Qd_VNECRxVGSW_XQJOGh5tMOrCtPhbN5Ep_k7aBCegbI0wrsis1m2?gv=true"',
    'href="https://tennistmate.setmore.com"'
)

# 4. Remove rylan from default coaches and replace google calendar with setmore
content = re.sub(
    r'venmo: "Aden-Ingwerson",\s*calendar: "https://calendar\.google\.com/calendar/appointments/schedules/AcZssZ1aMaYFfS5CqV2J442kfd7Qd_VNECRxVGSW_XQJOGh5tMOrCtPhbN5Ep_k7aBCegbI0wrsis1m2\?gv=true",\s*stripeCoaching: "https://buy\.stripe\.com/7sY7sD22CeHQdWs9zhaZi01",.*?weeklyPrice: "60"\s*}\s*\}',
    """venmo: "Aden-Ingwerson",
      calendar: "https://tennistmate.setmore.com",
      stripeCoaching: "https://buy.stripe.com/7sY7sD22CeHQdWs9zhaZi01",
      coachingPrice: "25"
    }
  }""",
    content,
    flags=re.DOTALL
)

# 5. Remove Rylan from saveCoaches
content = content.replace('if (id !== "aden" && id !== "rylan") custom[id] = coach;', 'if (id !== "aden") custom[id] = coach;')

# 6. Update the JS pricing bar
content = re.sub(
    r'pricingBar\.innerHTML = `.*?`;',
    'pricingBar.innerHTML = `<div class="price-item" style="width: 100%; border-right: none; justify-content: center;"><span>🎾 Single 1-Hour Lesson</span><strong id="singleLessonPriceDisplay">$` + (coach.coachingPrice || "25") + ` / hr</strong></div>`;',
    content,
    flags=re.DOTALL
)

# 7. Update Stripe HTML Buttons
content = re.sub(
    r'<div class="stripe-buttons">.*?</div>',
    """<div class="stripe-buttons">
              <a id="stripeCheckoutBtn" href="https://buy.stripe.com/7sY7sD22CeHQdWs9zhaZi01" class="stripe-btn" target="_blank">1-Hour Lesson ($25)</a>
            </div>""",
    content,
    flags=re.DOTALL
)

# 8. Update JS Stripe Buttons Logic
content = re.sub(
    r"const stripeButtons = document\.querySelectorAll\('\.stripe-btn'\);.*?\}",
    """const stripeBtn = document.getElementById('stripeCheckoutBtn');
    if (stripeBtn) {
      stripeBtn.href = coach.stripeCoaching || "https://buy.stripe.com/7sY7sD22CeHQdWs9zhaZi01";
      stripeBtn.innerText = `1-Hour Lesson ($` + (coach.coachingPrice || '25') + `)`;
    }""",
    content,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
