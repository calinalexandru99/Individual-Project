import React from "react";
import {createMuiTheme, ThemeProvider} from "@material-ui/core/styles";
import {SnackbarProvider} from "notistack";
import Router from "./Router";

const theme = createMuiTheme({
    palette: {
        primary: {
            main: "#EFEFEF",
        },
        secondary: {
            main: "#A9A9A9",
        },
    },
});

const App: React.FC = () => {
    return (
        <ThemeProvider theme={theme}>
            <SnackbarProvider maxSnack={2} preventDuplicate>
                <Router/>
            </SnackbarProvider>
        </ThemeProvider>
    );
};

export default App;