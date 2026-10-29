# Uniformly bounded physical quantum meridians through every actual braid

28 October 2026. The particular Heisenberg meridian matrices of the
ORIGINAL quantum crossing are uniformly bounded in N along any fixed
signed braid word, despite the possible exponential condition number
of its crossing matrices. The reason is the EXACT quantum Hurwitz law:
their conjugates are fixed Nielsen words in the initial meridians,
whose inverses have a bounded polynomial formula.

Their entries and adjoints asymptotically commute in operator norm.
Consequently every positive Gram moment limit has compact, honest
SL2 free-group/braid-graph support, including Gauss-chart boundaries.
This does NOT impose the original knot closure on such a positive
state or identify singular atomic shape phases with that support.
Those are explicit remaining requirements for a sharp upper bound.

## 1. The original complete-head observables form a bounded star family

Use the actual balanced factorial basis, N>=2, d=N-1,
q=exp(pi*i/N), Q=q^2, x=-q^(-1), rho=q-q^(-1). Put

    K=x Z^(-1), e=q rho^2 E, f=F,
    Z w_a=Q^a w_a.

These are the ORIGINAL finite quantum-group matrices. Explicitly

    f w_a=(1-Q^(a+1))w_(a+1), a<d, f w_d=0,
    e w_(a+1)=(x^(-1)-xQ^(-a))w_a, a<d.

In the actual flat positive head metric,

    ||K||=||K^(-1)||=1, ||e||,||f||<=2,
    K^*=K^(-1), e^*=x f, f^*=x e.                 (1)

The last identities follow entrywise using xQ=x^(-1). They do
not assert unitarity of the original braiding or positivity of its
pivotal closing, both of which have separate exact obstructions.

The scaled relations are

    Ke=QeK, Kf=Q^(-1)fK,
    [e,f]=(Q-1)(K-K^(-1)),
    fe=c-QK-K^(-1), c=x^(-1)+Qx.                  (2)

Thus commutators among e,f,K,K^(-1) and ALL their adjoints have
norm O(|Q-1|)=O(1/N). Different heads commute exactly. There is
no inverse rho or factorial in these estimates.

## 2. Bounded matrices and polynomial inverses

On an auxiliary two-dimensional space define the actual L matrices

    L_+=[[K,e],[0,I]], L_-=[[I,0],[-Kf,K]],
    L_-^(-1)=[[I,0],[f,K^(-1)]],
    G=L_-^(-1)L_+=[[K,e],[fK,fe+K^(-1)]].          (3)

All L matrices and their inverses have norm at most 3: each is a
unitary block diagonal plus an off-diagonal block of norm at most 2.
Consequently

    ||G||,||G^(-1)||<=9.

The exact quantum identity already proved from the original entries is

    G^2-cG+QI=0, G^(-1)=Q^(-1)(cI-G).             (4)

It supplies an alternative polynomial inverse, without choosing a
Gauss face denominator or inverting a nilpotent root shift.

For b heads set P_(j-1)=L_(-,j-1)...L_(-,1) and

    H_j=P_(j-1)^(-1)G_j P_(j-1), 1<=j<=b.        (5)

These are the actual based meridians (the physical SL2 lift is -H_j).
Before any braid action,

    ||H_j||,||H_j^(-1)||<=9^j<=C_b, C_b=9^b.     (6)

All entries are fixed-degree polynomials in the head observables (1),
with coefficients bounded uniformly in N. Their inverse entries
also have this property by (4).

## 3. Exact all-word Heisenberg transport and its uniform bound

Let B_i be the ORIGINAL checked crossing on heads i,i+1, with its
full common Cartan scalar either included or retained in the unchanged
external line. The direct finite proof in
[the shared quantum flags](actual_shared_quantum_flags_and_charged_exchange.md)
gives the exact two-head identities. They extend to (5) as

    Ad_(B_i) H_i=H_(i+1),
    Ad_(B_i) H_(i+1)=H_(i+1)H_iH_(i+1)^(-1),
    Ad_(B_i) H_j=H_j for j!=i,i+1.                (7)

Indeed the earlier prefix commutes with B_i. For later heads the
two adjacent L_- factors in the prefix have their product preserved
by the same original Hopf intertwining; thus the later prefix is
unchanged. The inverse crossing gives

    Ad_(B_i^(-1)) H_i=H_i^(-1)H_(i+1)H_i,
    Ad_(B_i^(-1)) H_(i+1)=H_i.                    (8)

No inverse of B is estimated by its operator norm. Repeatedly
substituting (7)-(8) expresses, for EVERY actual signed prefix W of
length m,

    W H_j W^(-1)=w_(W,j)(H_1,...,H_b),            (9)

where w is the explicit free-group Nielsen word. Its unreduced
length is at most 3^m; free cancellation can only improve it.
Therefore, uniformly for all levels N,

    ||W H_j W^(-1)||, ||(W H_j W^(-1))^(-1)||
                              <=C_b^(3^m).       (10)

The bound is intentionally coarse and may be large in the fixed
diagram. Its point is independence of N. All full Cartan/framing/
peripheral scalars remain those of W; its scalar line cancels only
in this genuine conjugation identity.

Each entry on the right of (9), and its adjoint, is a fixed-degree
bounded polynomial in (1). Leibniz expansion of a commutator and
(2) now prove, for ANY two such entries at ANY two prefixes,

    ||[A_N,B_N]||, ||[A_N,B_N^*]||<=C_(b,W)/N.     (11)

Thus the full finite family of transported physical meridian
observables is uniformly bounded and asymptotically commuting as a
star family. A general Heisenberg conjugate of an arbitrary coupon
does not enjoy (10); the exact Nielsen relation is essential here.

## 4. What every positive Gram limit actually supports

Take ANY positive trace-class Gamma_N of trace one on the initial
b-head Hilbert space. This could be a normalized Gram of a specified
annotated network if that construction is available; no positive
pivotal closing is being assumed. For the fixed family above every
polynomial moment is uniformly bounded, so a subsequence has all
moments convergent.

Equation (11) lets these limits be regarded as a functional on the
COMMUTATIVE polynomial star algebra of the limiting entries. It is
positive because for every polynomial p,

    lim Tr(Gamma_N p_N^*p_N)>=0.

It has a compact representation. To see the needed boundedness
directly, use real and imaginary coordinate operators. Each has
norm at most a fixed C. Thus in its polynomial GNS inner product,
multiplication by each real coordinate is a commuting selfadjoint
operator of norm at most C: positivity of C^2-X_N^2 passes to the
limit. Their joint spectrum is compact and represents the moments
by a positive measure. This uses the actual operator bounds, not
normalized expectations of a nonpositive source.

At any character of that commutative algebra let k,e,f denote a
head's values. Equations (1)-(2) imply

    |k|=1, f=-conjugate(e), ef+k+k^(-1)=-2.

The commuting matrix g from (3) therefore has determinant one and
trace -2. Its based versions h_j in (5) are genuine SL2 matrices,
including the central value -I. All their inverses remain regular.
The exact identities (7)-(9) show that the time-indexed character
matrices are precisely the honest free-group Hurwitz braid graph.
This statement persists when a local Gauss coordinate or flag
cross-ratio chart degenerates. It does not require a bounded inverse
of that chart's denominator.

For example, if a SPECIFIED positive annotated state additionally
obeyed the actual closed-meridian matching equations in mean square,
its limiting measure would be supported on honest knot representations.
For a polynomial matrix constraint F, the statement follows from
Tr(Gamma_N F_N^*F_N)->0 and positivity. Establishing that property for
the ORIGINAL relative closing is a remaining theorem, not a consequence
of (10) or an assertion of this note.

## 5. Why final cut vectorization does not supply those constraints

The actual assembled knot cut is C_K=f_(K,N)I. When it is nonzero,
its normalized vectorized Gram is EXACTLY

    |vec C_K><vec C_K|/||C_K||_HS^2
                       =|vec I><vec I|/N.         (12)

It is the same cut state for every knot. The scalar norm stores the
unknown period; the normalized state by itself contains no interior
meridian or atomic-shape data. Such data must be added as a specified
bounded observable/source lift, rather than inferred from (12).

Retaining all internal coupon moments is possible algebraically, but
the original closing is not a positive multiplicative compression:
its canonical nilpotent Pi satisfies ptr_g(Pi)=I and Pi^2=0, while
ptr_g(I)=0. The [actual positivity obstruction](actual_quantum_source_positivity_obstruction.md)
therefore remains relevant. The polynomial norm of that extension
helps retain it; it does not automatically make its positive Gram
impose all original closure equations.

Finally, honest physical braid-graph support alone does not identify
the JOINT atom-shape limit at singular face denominators. A boundary
comparison must retain those shapes and their regulator, not merely
bounded physical matrices. The saturated critical compactification
theorem already bounds the regulator on the genuine critical joint
closure; this note does not prove that every source boundary belongs
to that closure.

The unconditional advance is (9)-(11): the specific physical
Heisenberg meridians need no uncontrolled braid-condition-number
estimate. No sharp whole-period upper bound is asserted here.

[Audit](../experiments/audit_actual_bounded_quantum_meridians.py):
literal original signed prefixes, all based quantum matrices, exact
Nielsen substitution, polynomial inverses and direct complex star/
commutator bounds. It retains both crossing signs and original
Cartan factors in the matrix comparisons.
