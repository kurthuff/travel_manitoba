"""
Project Path Configuration
--------------------------
Centralized path management for the Travel Manitoba project.

Usage:
    from paths import raw, processed, powerbi
    
    # Load data
    df = pd.read_csv(raw() / 'airport_data.csv')
    
    # Save processed data
    df.to_csv(processed() / 'airport_clean.csv')
"""

from pathlib import Path

# Project root is one level up from scripts/
project_root = Path(__file__).resolve().parent.parent


# Data directories
def raw() -> Path:
    """Original, immutable data files."""
    return project_root / "data" / "raw"


def interim() -> Path:
    """Intermediate transformation outputs."""
    return project_root / "data" / "interim"


def processed() -> Path:
    """Cleaned data ready for Power BI."""
    return project_root / "data" / "processed"


def external() -> Path:
    """Data from third-party sources."""
    return project_root / "data" / "external"


# Working directories
def notebooks() -> Path:
    """Jupyter notebooks for EDA."""
    return project_root / "notebooks"


def scripts() -> Path:
    """ETL scripts and utilities."""
    return project_root / "scripts"


# Output directories
def outputs() -> Path:
    """All analysis outputs."""
    return project_root / "outputs"


def powerbi() -> Path:
    """Power BI dashboard files."""
    return project_root / "outputs" / "powerbi"


def reports() -> Path:
    """Generated reports and documentation."""
    return project_root / "outputs" / "reports"


def figures() -> Path:
    """Charts and visualizations."""
    return project_root / "outputs" / "figures"


# Documentation
def docs() -> Path:
    """Project documentation."""
    return project_root / "docs"


# Utility function
def ensure_dirs():
    """Create all project directories if they don't exist."""
    dirs = [
        raw(), interim(), processed(), external(),
        notebooks(), scripts(),
        outputs(), powerbi(), reports(), figures(),
        docs()
    ]
    for directory in dirs:
        directory.mkdir(parents=True, exist_ok=True)
    print(f"✓ All directories created under: {project_root}")


if __name__ == "__main__":
    # Run this file to create all directories
    print(f"Project Root: {project_root}")
    ensure_dirs()