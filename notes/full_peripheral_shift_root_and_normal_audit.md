# Audit of the full peripheral shift on root fibers and normal germs

27 October 2026. The corrected full-normalization paragraph in
[the partial support theorem](partial_geometric_support_theorem.md),
Section 5, passes. Its root-family and geometric-symbol conclusions
are unchanged. The whole q-normal source requires the additional
power-character factor below.

Keep the original line

    d_N(M)=epsilon_N M^(N-1)(M^2-1)/(M^(2N)-1),

with its actual rational-map/source lattice at canceled or uncanceled
divisors. Direct division gives EXACTLY

    g_N(q,M)=d_N(qM)/d_N(M)
      =q^(N-1)(q^2 M^2-1)/(M^2-1)
                             *(M^(2N)-1)/(q^(2N)M^(2N)-1).

The fixed root phase epsilon_N cancels; it has not been reset.
For N_N=d_N F_N, the correct gauge of an operator annihilating
F_N is d_N D d_N^-1. Thus its ordered substitution is

    T -> g_N^-1 T,
    T^r -> product_(j=0)^(r-1) g_N(q,q^jM)^-1 T^r.

These products follow from T f(M)=f(qM)T, not a commutative
substitution for powers.

With independent retained powers z=q^N,w=M^(2N), the whole factor is

    g_N=q^-1 z (q^2 M^2-1)/(M^2-1)*(w-1)/(z^2w-1).

The meridian Ore step MUST act by

    sigma(M)=qM, sigma(z)=z, sigma(w)=z^2w.

In particular w is fixed by this step only AFTER restriction
to the physical root character z=-1. There that restriction is
the meromorphic meridian-germ identity

    g_bar=-q^-1(q^2 M^2-1)/(M^2-1).

The common w-1 cancels as a rational identity on the root fiber.
Its complete lattice is still required at norm-zero intersections;
g_bar itself has a pole at M=1 for N>1 and must not be evaluated
there as a regular unit. This agrees with the original source guard.

Consequently the ordered root gauge in the partial theorem is
correct on every actual root meridian family. Its generic-M
classical symbol has g_bar -> -1, so the preexisting geometric
factor becomes A_geo(M,-L_full) in that FULL ROOT shift convention.
The same applies to the Fourier and fixed-input root families;
neither uses an asserted whole-normal identification.

The distinction is visible before any asymptotic analysis:

    g_N/g_bar=-z(w-1)/(z^2w-1),
    (g_N/g_bar)|_(z=-1)=1,
    D_z log(g_N/g_bar)|_(z=-1)=-(w+1)/(w-1).

On the actual whole fixed-N power graph this gives

    [D_q log g_N-D_q log g_bar]|_(q=q_N)
                  =-N (M^(2N)+1)/(M^(2N)-1),

where D_q=q partial_q with M fixed. Hence equality on the entire
root MERIDIAN germ does not equate its q-normal jets. The discrepancy
retains exactly the peripheral character and its norm divisor.

Finally g_N -> +1 as q->1 at FIXED N and generic M. This is a
different specialization from the root-character classical symbol
g_bar -> -1. The latter is the statement of the root-family support
theorem; one may not transfer it to a whole fixed-N gauge by
forgetting z,w or changing their Ore action. No conclusion about
the final selected geometric period is added by this audit.
