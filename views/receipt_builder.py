"""Receipt builder page: a thin UI over logic.receipt_builder."""

import streamlit as st

from logic.receipt_builder import ReceiptItem, TAX_RATE, build_receipt

SESSION_ITEMS_KEY = "receipt_items"
DEFAULT_ITEM_PRICE = 0.0
MIN_ITEM_PRICE = 0.0
PRICE_STEP = 0.50
PERCENT_DIVISOR = 100


def render() -> None:
    """Render the receipt builder page."""
    st.title("Receipt Builder")
    st.write("Build a café check item by item.")

    if SESSION_ITEMS_KEY not in st.session_state:
        st.session_state[SESSION_ITEMS_KEY] = []

    item_name = st.text_input("Item name")
    item_price = st.number_input(
        "Item price ($)", min_value=MIN_ITEM_PRICE, value=DEFAULT_ITEM_PRICE, step=PRICE_STEP
    )

    if st.button("Add item"):
        if not item_name.strip():
            st.warning("Enter an item name before adding it.")
        else:
            st.session_state[SESSION_ITEMS_KEY].append(
                {"name": item_name.strip(), "price": float(item_price)}
            )

    items: list[ReceiptItem] = st.session_state[SESSION_ITEMS_KEY]
    receipt = build_receipt(items, TAX_RATE)

    st.subheader("Order")
    if not items:
        st.write("No items yet.")
    for item in items:
        st.write(f"{item['name']}: ${float(item['price']):.2f}")

    st.subheader("Receipt")
    st.write(f"Subtotal: ${receipt['subtotal']:.2f}")
    st.write(f"Tax ({TAX_RATE * PERCENT_DIVISOR:.0f}%): ${receipt['tax']:.2f}")
    st.metric("Total", f"${receipt['total']:.2f}")