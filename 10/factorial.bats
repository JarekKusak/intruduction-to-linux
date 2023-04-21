#!/usr/bin/env bats

check_it() {
    local num="$1"
    local expected="$2"

    # Negativní input
    if [ "$num" -lt 0 ]; then
        echo "Error: Input must be a non-negative integer."
        return 1
    fi

    # Žádný input
    if [ -z "$num" ]; then
        echo "Error: No input provided."
        return 1
    fi

    # Není číslo v inputu
    if ! echo "$num" | grep -Eq '^[0-9]+$'; then
        echo "Error: Input must be a non-negative integer."
        return 1
    fi

    run factorial "$num"

    test "$output" = "$expected"
}

for i in {0..31}; do
    @test "factorial $i" {
        check_it "$i" "$(factorial "$i")"
    }
done
