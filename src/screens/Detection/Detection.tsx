import React, {useState} from "react";
import TopBar from "../../components/TopBar";
import {Button, Card, createStyles, makeStyles, TextField, Typography} from "@material-ui/core";
import { useHistory } from "react-router-dom";

const useStyles = makeStyles((theme) =>
    createStyles({
        container: {
            height: "100%",
            flex: 1,
            display: "flex",
            justifyContent: "space-evenly",
            alignItems: "center",
            marginTop: "50px",
            [theme.breakpoints.down("sm")]: {
                flexDirection: "column",
            },
            [theme.breakpoints.up("md")]: {
                flexDirection: "row",
            },
        },
        card: {
            height: "80%",
            width: "80%",
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-evenly",
            padding: 8,
        },
        text: {
            textAlign: "center",
            [theme.breakpoints.only("xs")]: {
                fontSize: "1rem",
            },
            [theme.breakpoints.only("sm")]: {
                fontSize: "1.25rem",
            },
            [theme.breakpoints.only("md")]: {
                fontSize: "1.5rem",
            },
            [theme.breakpoints.up("lg")]: {
                fontSize: "2rem",
            },
        },
        button: {
            height: "60px",
            width: "150px",
            fontSize: "2rem",
        },
        buttonContainer: {
            justifyContent:"center",
            alignItems: "center",
            display:"flex",
        }
    })
);

const Detection: React.FC = () => {

    const [text, setText] = useState("");
    const [error, setError] = useState(false);

    const history = useHistory();

    const onTextChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setError(false);
        setText(event.target.value);
    };

    const onCheckClick = () => {
        if (text === "") {
            setError(true);
        } else {
            history.push("/detection/feedback");
        }
    }

    const classes = useStyles();

    return (
        <>
            <TopBar showBack/>
            <div className={classes.container}>
                <Card className={classes.card}>
                    <Typography className={classes.text}>
                        In the box below you can enter the text that you want to evaluate
                    </Typography>
                    <TextField
                        margin="dense"
                        label="Insert your text here"
                        required
                        size="medium"
                        multiline
                        type="text"
                        error={error}
                        helperText={error ? "Text box cannot be empty" : ""}
                        value={text}
                        onChange={onTextChange}
                    />
                    <div className={classes.buttonContainer}>
                        <Button variant="contained" color="primary" onClick={onCheckClick} className={classes.button}>
                            Check
                        </Button>
                    </div>

                    <Typography className={classes.text}>
                        After pressing the Check button you will be redirected to a new page where the results of the
                        evaluation will be shown.
                    </Typography>
                </Card>
            </div>
        </>
    );
};
export default Detection;