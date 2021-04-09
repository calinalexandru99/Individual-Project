import React from "react";
import { Button, Typography } from "@material-ui/core";
import { createStyles, makeStyles } from "@material-ui/core/styles";
import { useHistory } from "react-router-dom";

const useStyles = makeStyles((theme) =>
    createStyles({
        container: {
            height: "100%",
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-evenly",
            alignItems: "center",
        },
        errorText: {
            fontSize: "3rem",
            fontWeight: "bold",
            [theme.breakpoints.only("xs")]: {
                fontSize: "150%",
            },
            [theme.breakpoints.only("sm")]: {
                fontSize: "1.5rem",
            },
            [theme.breakpoints.up("md")]: {
                fontSize: "3rem",
            },
        },
        returnButton: {
            borderRadius: 20,
            [theme.breakpoints.only("xs")]: {
                width: 300,
                height: 50,
                fontSize: "1rem",
            },
            [theme.breakpoints.only("sm")]: {
                width: 350,
                height: 58,
                fontSize: "1rem",
            },
            [theme.breakpoints.up("md")]: {
                width: 370,
                height: 61,
                fontSize: "1.25rem",
            },
        },
    })
);

const InvalidPage: React.FC = () => {
    const history = useHistory();

    const classes = useStyles();

    const onReturnClick = () => history.push("/");

    return (
        <div className={classes.container}>

            <Typography className={classes.errorText}>Page Not Found</Typography>

            <Button
                className={classes.returnButton}
                variant="contained"
                color="primary"
                size="large"
                onClick={onReturnClick}
            >
                Go To Main Menu
            </Button>
        </div>
    );
};

export default InvalidPage;