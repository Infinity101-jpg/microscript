new::num::0



forever
    if::btn_a
        if::num::<=::9
            change::num::num+1;
        end
        if::num::==::10
            change::num::0;
        end
    end
    if::btn_b
        if::num::>=::0
            change::num::num-1;
        end
        if::num::==::-1
            change::num::9;
        end
    end
    printresp::num
end
