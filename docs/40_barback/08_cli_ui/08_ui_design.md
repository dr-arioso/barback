
# UI Design (Future Roadmap)

A cross-platform UI is planned for Barback.

### Core UI Features
- **Drag & drop bottle identification**
- **Real-time classification visualization**
- **Tag browser** (flavor, cocktail roles, origin, production method)
- **Conflict resolution prompts**
- **Full bottle editor**
- **Inventory views** (grid, list, category-tree)
- **Shelf mapping** (optional in future)

### UI Technology Options
- Electron
- PySide/Qt
- Web UI w/ local backend
- Mobile wrappers (Kivy or React Native)

### Core Architecture
UI talks to a local Barback API server, ensuring a clean separation.
