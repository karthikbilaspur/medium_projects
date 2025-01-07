// Navigation menu toggle
document.addEventListener("DOMContentLoaded", function () {
    const navToggle = document.querySelector(".nav-toggle");
    const navMenu = document.querySelector(".nav-menu");
  
    navToggle.addEventListener("click", function () {
      navMenu.classList.toggle("show");
    });
  });
  
  // Appointment date picker
  const dateInput = document.getElementById("appointment_date");
  dateInput.type = "date";
  
  // Vaccination reminder timer
  const reminderTime = document.getElementById("reminder_time");
  const countdown = () => {
    const appointmentDate = new Date(reminderTime.dataset.appointmentDate);
    const currentTime = new Date();
    const timeDifference = appointmentDate.getTime() - currentTime.getTime();
  
    if (timeDifference > 0) {
      const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
      const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);
  
      reminderTime.innerHTML = `${days} days, ${hours} hours, ${minutes} minutes, ${seconds} seconds`;
    } else {
      reminderTime.innerHTML = "Appointment time has passed!";
    }
  };
  
  countdown();
  setInterval(countdown, 1000);