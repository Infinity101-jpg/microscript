new::a::false

forever

    new::lp::0

    loop::9

        if::a::==::true
            forever
                printf::" "
            end
        end

        change::lp::lp+1
        printf::lp
        if::btn_a
            change::a::true
        end
    end
end
