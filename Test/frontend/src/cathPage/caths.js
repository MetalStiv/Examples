import React, { useEffect, useState } from 'react';
import Header from '../common/header'
import Footer from '../common/footer'
import {cathAxios} from '../common/constants';

function Caths(props){
    const [caths, setCaths] = useState([])

    useEffect(() => {
        cathAxios.get('/getCaths')
            .then(response => setCaths(response.data))
    }, [])

    return (
        <React.Fragment>
            <Header />
            {caths.map(cath => <p>{cath.short_name} - {cath.name}</p>)}
            <Footer />
        </React.Fragment>
    )
}

export default Caths