import React, { Component } from 'react'
import { Query } from 'react-apollo'
import gql from 'graphql-tag'
import client from './apollo'


export const GET_BIDS = gql`
	query GET_BIDS{
		allBids {
			edges {
				node{
					channel
				}
			}
		}
	}
`

export default class RowViewer extends Component {
	render(){
		return(
			<div>
				<Query query={GET_BIDS}>
					{({ loading, data, error })}
				</Query>
			</div>
		);
	}
};