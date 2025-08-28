const evenOdd = () => {
    let raw = result.value.trim();

    if (!raw) {
        result.value = "Please enter something";
        return;
    }


    result.value = number % 2 === 0 ? `${number} → Even` : `${number} → Odd`;
};
