# Eigenvalue counting for the actual positive endpoint matrix

Private continuation, 1 November 2026. This preserves an auxiliary
argument while the manuscript audit is in progress. It is not a new
whole-source or volume theorem. The inverse and total trace below were
already known in `notes/actual_matching_edge_polynomial_endpoint_control.md`;
the proposed extension is a bound for every ordered eigenvalue.

Let theta=pi/N and 1<=a<=floor((N-1)/2). The actual Hermitian endpoint
matrix H has diagonal

    d_i=1/(cos(i theta) cos((i+1)theta)),  0<=i<a,

and off-diagonal squared modulus

    beta_j=sin(j theta)^2 /
      (cos(j theta)^2 sin((2j-1)theta) sin((2j+1)theta)), 1<=j<a.

Both H_+ and H_- differ only by phases in these off-diagonal entries.
Their positive pivots are

    p_i=sin((i+1)theta)/(cos((i+1)theta) sin((2i+1)theta)).

A diagonal unitary gauge makes every off-diagonal negative real. Write
s_i=sin((2i+1)theta), w_i=tan((i+1)theta), z_i=sqrt(s_i)y_i,
and y_a=0. Since sqrt(beta_(i+1))/p_i=sqrt(s_i/s_(i+1)),
the exact Cholesky identity gives

    z*Hz = sum_(i=0)^(a-1) w_i |y_i-y_(i+1)|^2,
    ||z||^2 = sum_(i=0)^(a-1) s_i |y_i|^2.

This includes the original last pivot and its right Dirichlet endpoint;
there is no added row.

On a consecutive block b<=i<=c of length L, with a natural left
boundary and y_(c+1)=0, the inverse trace in the weighted norm is

    sum_(j=b)^c cot((j+1)theta) sum_(i=b)^j sin((2i+1)theta).

The inner sum equals

    sin((j-b+1)theta) sin((j+b+1)theta)/sin(theta).

Because (j+1)theta<pi/2 and b<=j, the second sine is at most
2 sin((j+1)theta). Each summand is therefore at most 2(j-b+1),
and the block trace is at most L(L+1). Positivity implies that the
block's least eigenvalue is at least 1/[L(L+1)].

For 1<=k<=a impose k-1 coordinate zeros. Place them so the k remaining
blocks of free coordinates have length at most floor(a/k); empty
blocks are allowed. Discard only the nonnegative left-boundary
energies. Each block retains its right Dirichlet term. On this
codimension k-1 subspace the Rayleigh quotient is at least

    1/[floor(a/k)(floor(a/k)+1)] >= k^2/(2a^2).

The minimax principle gives, with eigenvalues in increasing order,

    lambda_k(H_+)=lambda_k(H_-) >= k^2/(2a^2).

This derivation was separately checked by the coherent-partner agent.
The full inverse trace is the earlier exact formula
sin(a theta)sin((a+1)theta)/(2sin(theta)^2); its novelty is not claimed.

For epsilon>=0, the counting bound implies

    det(I+epsilon H^(-1))
      <= product_(k=1)^a (1+2a^2 epsilon/k^2)
      <= exp(pi sqrt(2) a sqrt(epsilon)).

Indeed the decreasing function log(1+B^2/x^2) has integral pi B on
(0,infinity); the sum at positive integers is at most that integral.
No lower bound on a/N is required, and both parities are included.

For M=bI+xH_-/2+yH_+/2 with nonnegative faces and x>=r>0 (or y>=r),
one obtains lambda_k(M)>=r k^2/(4a^2) and

    det(I+epsilon M^(-1)) <= exp(2pi a sqrt(epsilon/r)).

For arbitrary complex E with operator norm <=B, exterior powers give

    |det(M+uE)| <= det(M) det(I+|u|B M^(-1)).

Use |Tr wedge^j(M^(-1)E)| <= B^j e_j(lambda(M)^(-1)); do not
replace this by an unsupported Loewner inequality for the absolute
value of M^(-1/2) E M^(-1/2).

For fixed Hermitian E, its eigenbasis expansion writes det(M+uE) as
a signed sum of stable compression determinants, with positive
majorant det(M+|u||E|). This is only a conditional algebraic route:
the actual varying signed source has not been shown to be such a
uniformly controlled matrix perturbation. Pointwise positive-radius
bounds also do not by themselves preserve cancellation after the
shared coefficient extraction.

The already existing note
`research_cap_cross_two_spectrum_neighborhood_stability.md` proves
neighborhood stability of a particular internal two-port contraction
by a different exact recurrence. Its incidence assumption does not
cover an arbitrary exterior with additional incidences. It must be
consulted before extending the present argument to that special case.
