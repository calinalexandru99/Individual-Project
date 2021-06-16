import React, { ReactNode } from "react";

interface PanelProps {
    value: number;
    index: number;
    children: ReactNode;
}

const Panel: React.FC<PanelProps> = ({ children, value, index }: PanelProps) => {
    if (value !== index) {
        return null;
    }

    return <>{children}</>;
};

export default Panel;