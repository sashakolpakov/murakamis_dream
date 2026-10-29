# Exact coherent turn reduction in the original Newton source

29 October 2026. The full original Newton alphabet obeys a projective
modular relation, with its Cartan scalar retained. It removes arbitrary
numbers of redundant twist/turn packets BEFORE a norm estimate. In one
arbitrary-length class the complete reflected original source is exactly
1 or N and has zero exponential rate. A same-sign run of two-crossing
packets reduces to one twist with explicit boundary adapters. These are
source-exact coherent reductions, not a new hyperbolic-volume family.

## 1. All-input relation, including the original Cartan line

Use the COMPLETE Newton packet of
[the positive turn metric](actual_newton_turn_positive_gram.md).
Let T=T_1, P=P_rev, d=N-1, q=exp(pi i/N), Q=q^2,
kappa=q^(d^2/2), and nu_j=(-1)^j Q^(j(j+1)/2). Its actual entries are

    T_ij=kappa nu_j (-q)^(i-j) [i choose j]_Q, i>=j,
    T^(-1)=conjugate(T).

All matrices below act on the FULL N-dimensional Newton packet,
including every original confluent derivative. Put

    theta_N=kappa^3(-q)^d, |theta_N|=1.

Then

    T P T=theta_N P T^(-1)P,
    (T P)^3=theta_N I.                                    (1)

Here P is the genuine unscaled physical turn in this packet. No
eigenvalue-only quotient or assumed ordinary positive trace is used.

For a finite own proof of (1), the Gaussian identity needed is

    sum_(k=0)^i (-1)^k Q^(k(k-1)/2-jk)
                    [i choose k]_Q [j+k choose j]_Q
       =(-1)^i Q^(i(i-1)/2-ij) [j choose i]_Q.             (2)

To prove it, expand

    [j+k choose j]_Q=(Q^(k+1);Q)_j/F_j
      =F_j^(-1) sum_(l=0)^j
           (-1)^l Q^(l(l+1)/2)[j choose l]_Q Q^(kl).

The finite binomial theorem performs the inner k sum as
(Q^(l-j);Q)_i. If i>j every term is zero. If i<=j, only l<=j-i
survive; insert

    (Q^(l-j);Q)_i
      =(-1)^i Q^[-i(j-l)+i(i-1)/2] F_(j-l)/F_(j-l-i).

The remaining sum is

    sum_(l=0)^(j-i) (-1)^l Q^[l(l+1)/2+il]
                         /(F_l F_(j-i-l))
      =(Q^(i+1);Q)_(j-i)/F_(j-i)=[j choose i]_Q.

This proves (2) by two finite binomial expansions. At the root every
denominator used here has index<N. If j+k>=N the product expression
for [j+k choose j] is zero and exactly supplies the original cutoff.

Now use the exact root reflection

    [d-k choose j]_Q=nu_j^(-1) Q^(-jk)[j+k choose j]_Q.

The (i,j) entry of TPT becomes kappa^2(-q)^(i+d-j) times the
left side of (2). For i>j it is zero. For i<=j, the reflected inverse
entry is

    (P T^(-1)P)_ij
       =kappa^(-1) nu_j^(-1)(-q)^(-(j-i))
                                    nu_(j-i)[j choose i]_Q.

Since nu_(j-i)/nu_j=(-1)^i Q^[i(i-1)/2-ij], (2) gives (1)
entry by entry. Thus all repeated-root normal data are retained.

## 2. An arbitrary-turn complete original source with an exact rate

Let C=TP and let 1=e_0 be the original numerator-source vector.
The first and last T columns give

    C e_0=kappa e_d,
    C^2 e_0=kappa^2 ((-q)^i)_(i=0)^d.

Together with (1), for every integer h,

    C^(3h)e_0=theta_N^h e_0,
    C^(3h+1)e_0=theta_N^h kappa e_d,
    C^(3h+2)e_0=theta_N^h kappa^2 ((-q)^i)_i.              (3)

The exact positive Newton metric consequently gives, for EVERY N,

    ||C^m 1||^2 = 1, m=0 or1 mod3;
                  N, m=2 mod3.                            (4)

Its literal adjoint-word closure, with the original unrestricted marked
cap and original cups, is exactly this norm by the positive metric
theorem. Thus the ENTIRE original reflected circuit has zero exponential
rate for arbitrarily many fixed turns. This does not say C is unitary:
(4) itself distinguishes norms1 and N. It says that these particular
large coherent turn networks are projectively periodic.

This is a useful normalization class, not a new hyperbolic class. It
shows why assigning an independent positive angle capacity to each
expanded crossing cannot give the actual rate even in the positive
reflected-source formulation.

## 3. Exact reduction of arbitrary same-sign two-crossing runs

There is also a useful reduction of the newly solved T_2 kernel:

    T^2 P=theta_N C T^(-1)C^(-1),
    (T^2P)^m=theta_N^m C T^(-m)C^(-1).                    (5)

These follow algebraically from (1), for all signed integers m.
The original source endpoint satisfies

    C^(-1)e_0=kappa^(-2)(-q)^(-d) T e_0.

Consequently the source-selected whole run is exactly

    (T^2P)^m e_0
      =theta_N^m kappa^(-2)(-q)^(-d)
                                  T P T^(1-m)e_0.         (6)

Thus a run with unbounded turn count has ONE retained turn and one
signed twist packet, with all original phase and endpoint adapters
displayed. The adapters are actual Newton operators; no assertion of
polynomial conditioning or unitarity is made for T. Equation (6) is an
exact coherent source reduction, not a sharp estimate for its remaining
mixed packet.

The same relation can remove unit digits inside a general rational
twist/turn word, with (1)'s scalar recorded. Reduced mixed-sign words
still contain real oscillatory interactions. Neither (5) nor finite
order of C diagonalizes those words or proves a geometric maximum.

## 4. Remaining analytic scope

The source of a genuinely reduced word is not determined by the
modular relation. In particular the norm of TPT_(-p)e_0 generally
contains a nontrivial coherent finite sum; unit nodal twist phases do
not make it a polynomially bounded operator. A new sharp variational
estimate must control that remaining packet and its integer marks,
then identify its full critical graph and regulator. This note proves
the exact reduction and the nonzero rate statement (4), not those
unproved assertions for arbitrary rational/arborescent sources.

Audit: [full original physical alphabet, all-input modular identity and actual reflected closures](../experiments/audit_actual_newton_coherent_turn_reduction.py).
