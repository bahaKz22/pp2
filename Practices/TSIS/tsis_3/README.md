# 🏎️ Racer Game - Advanced (TSIS 3)

This is an advanced version of the classic 2D racing game built with Python (Pygame). As part of the TSIS 3 assignment, the original game was completely overhauled: added modular architecture, dynamic obstacles, a power-up system, full menus, and JSON-based score saving.
> *Это продвинутая версия классической 2D-гонки на Python (Pygame). В рамках задания TSIS 3 оригинальная игра была полностью переработана: добавлена модульная архитектура, динамические препятствия, система бонусов (Power-ups), полноценное меню и сохранение результатов в JSON.*

---

## 🌟 Features / Основные возможности

* 🧩 **Modular Code / Модульный код:** 
  The project is well-structured into 4 main files. 
  *(Проект грамотно разбит на 4 основных файла: `main.py`, `racer.py`, `ui.py`, `persistence.py`.)*
* 🚗 **Dynamic Traffic & Obstacles / Динамический трафик и препятствия:** 
  Enemy cars and oil spills spawn randomly with safe spawn logic. 
  *(Вражеские машины и масляные лужи появляются случайно. Реализован безопасный спавн — объекты не появляются друг на друге.)*
* 🎁 **Power-Ups System / Система бонусов:**
  * ⚡ **Nitro:** Temporarily increases game speed (4s). *(Временное ускорение игры на 4 секунды с таймером).*
  * 🛡️ **Shield:** Protects from one collision. *(Защищает от одного столкновения).*
  * 🔧 **Repair:** Instantly restores one lost life. *(Мгновенно восстанавливает жизнь).*
* 📈 **Difficulty Scaling / Умная сложность:** 
  Game speed gradually increases as you progress. *(Скорость плавно увеличивается по мере прохождения).*
* 🖥️ **Full UI / Полноценный интерфейс:** 
  Username entry, Main Menu, Settings, Leaderboard, and Game Over screen with a Retry button. *(Ввод имени, Главное меню, Настройки, Таблица лидеров и экран Game Over с кнопкой Retry).*
* 💾 **Data Persistence / Сохранения:** 
  Settings and Top-10 Leaderboard are saved to `.json` files. *(Настройки и Топ-10 игроков сохраняются в локальные JSON-файлы).*

---

## 📂 Project Structure / Структура проекта

* `main.py` — Entry point / *Точка входа в программу*.
* `racer.py` — Core game engine / *Основной движок игры*.
* `ui.py` — Renders all menus and screens / *Отрисовка всех меню и кнопок*.
* `persistence.py` — JSON reading/writing / *Работа с файлами сохранений*.
* `assets/` — Media resources (images, music) / *Все медиа-ресурсы (картинки, звуки)*.

---

## 🚀 How to Run / Как запустить

1. Ensure you have Python 3.x installed. *(Убедитесь, что установлен Python 3.x).*
2. Install Pygame / *Установите Pygame*:
   ```bash
   pip install pygame