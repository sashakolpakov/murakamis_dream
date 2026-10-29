# Independent algebra audit of the ordinary-color positive trace bound

28 October 2026. This independently checks the positive path algebra used
in Section 2 of `regularized_kashaev_period.md`. No published volume,
Jones asymptotic, positivity theorem or recoupling identity is a premise.
The local path matrices, trace, projections, cabling and framing estimate
are proved below. The separate identification with the ORIGINAL reduced
ordinary-color cut is being audited in
`actual_ordinary_color_comparison_audit.md`.

Verdict: the path-algebra proof is correct. The estimates include every
color j<N, in particular j=N-1. The explicit arguments below fill in the
two compressed steps: the Jones--Wenzl square relation and multiplicative
trace of disjoint color projections.

## 1. Local matrices, without an imported positive trace

For N>=3 set theta=pi/N, q=exp(i theta), delta=q+q^(-1), and

    mu_a=sin((a+1)theta)/sin(theta), 0<=a<=N-2.

These weights are strictly positive. With mu_(-1)=mu_(N-1)=0 they obey
mu_(a-1)+mu_(a+1)=delta mu_a, including the two endpoints.
The Hilbert space H_m has its orthonormal basis the length-m walks
(a_0,...,a_m) in {0,...,N-2}, a_0=0, |a_i-a_(i-1)|=1.

The operator U_i is zero unless a_(i-1)=a_(i+1)=c. It then replaces
a_i by a neighbor a_i' of c with coefficient

    sqrt(mu_(a_i')mu_(a_i))/mu_c.                 (1)

It is real symmetric. On a fixed pair of equal outer neighbors its
nonzero block is vv^t/mu_c, with v_a=sqrt(mu_a). The neighbor identity
implies U_i^2=delta U_i.

Here is the complete adjacent-product calculation. In U_i U_(i+1) U_i,
suppose the original outer heights for the first U_i are c,c and
a_(i+2)=d. The middle operator forces the first replacement a_i'=d;
the final U_i forces the middle replacement a_(i+1)'=c. The three
coefficients multiply to

    sqrt(mu_(a_i)mu_d)/mu_c
       * mu_c/mu_d
       * sqrt(mu_d mu_(a_i''))/mu_c
      =sqrt(mu_(a_i)mu_(a_i''))/mu_c.

This is precisely U_i. All forced heights are allowed neighbors, so
no nonexistent boundary height or zero weight is divided by. The
opposite adjacent relation is identical. Distant U's commute since
they change distinct middle heights and share only fixed endpoints.

Consequently B_i=q^(1/2)I-q^(-1/2)U_i is unitary: the coefficient
of U_i in B_i B_i^* is delta-q-q^(-1)=0. Expanding its braid relation
reduces its difference to a multiple of

    q-(q+q^(-1))+q^(-1)=0.

This proves unitarity and braiding directly at the chosen principal root.

## 2. The weighted trace and both Markov identities

Define tau_m(A)=sum_paths mu_(a_m) A_(a,a). Every U_i and B_i
preserves a_m. Hence the positive diagonal matrix of endpoint weights
commutes with their algebra, and tau is a positive tracial functional.

For the included operator A on H_(m+1), summing over the last neighbor
b of a_m gives

    tau_(m+1)(A tensor I)=delta tau_m(A).          (2)

For the second identity, a diagonal contribution to (A tensor I)U_m
requires that the U_m replacement leave a_m unchanged, since A preserves
its m-th endpoint. U_m also forces a_(m+1)=a_(m-1). Its diagonal entry
is mu_(a_m)/mu_(a_(m-1)); multiplication by the trace weight cancels
the denominator. Every length-m prefix has exactly this allowed final
neighbor. Thus

    tau_(m+1)((A tensor I)U_m)=tau_m(A).          (3)

These arguments apply to arbitrary elements of the generated algebra,
not only its diagonal or commuting words.

The same identities determine the planar closure trace algebraically.
Indeed the elementary TL relations inductively imply

    TL_(m+1)=TL_m + TL_m U_m TL_m.

To reduce a word containing two U_m's, decompose its intervening TL_m
word into TL_(m-1) plus TL_(m-1)U_(m-1)TL_(m-1); commute the former
past U_m, then use U_m^2=delta U_m or U_m U_(m-1) U_m=U_m.
Traciality, (2) and (3) therefore recursively fix the trace on every
word, starting with tau_0(1)=1.

Closing a planar pairing diagram and assigning delta to each resulting
circle obeys the same relations and recursions: the square relation
creates one circle, the adjacent relation none. Hence it is that same
trace. In particular horizontal juxtaposition of two diagrams multiplies
their traces, since their closed circle sets are disjoint. By linearity,

    tau_(r+s)(A tensor B)=tau_r(A)tau_s(B).       (4)

This proves the product-color trace used below rather than assuming it.

## 3. Color projections through the last permitted color

Write [r]=sin(r theta)/sin(theta). Starting with p_0=p_1=I, set

    p_(m+1)=p_m-([m]/[m+1])p_m U_m p_m.          (5)

The first term is included on m+1 strands. Every denominator is positive
for m+1<=N-1. For m=1 the required square relation is simply
U_1^2=delta U_1, so no generator U_0 is needed. For m>=2 let
g=p_(m-1), c=[m-1]/[m], and f=p_m=g-cgU_(m-1)g. Then fg=gf=f,
and g commutes with U_m. Therefore x=fU_m f satisfies

    x^2=(delta-c)x=([m+1]/[m])x.                 (6)

The first equality follows by inserting f=g-cgU_(m-1)g between the
two U_m's and using the square/adjacent TL relations. More explicitly,
commuting g past U_m and using fg=f gives
fU_m fU_m=delta fU_m-c fU_m U_(m-1)U_m g=(delta-c)fU_m.
Multiplication on the right by f gives (6).
It follows that (5) is a selfadjoint idempotent and annihilates U_m
on both sides. Earlier U_i are already annihilated by f. Conversely
any vector killed by all internal U_i is fixed by p_(m+1), since
p_(m+1)-I lies in their generated ideal. This verifies the intended
common-kernel projection, with no generic semisimplicity assumption.

Use positivity, (2)--(3), idempotence and traciality to compute

    tau_(m+1)(p_(m+1))
      =delta tau_m(p_m)-([m]/[m+1])tau_m(p_m)
      =delta[m+1]-[m]=[m+2].                    (7)

In the middle line tau_(m+1)(p_m U_m p_m)=tau_m(p_m).
The base values tau_0(p_0)=[1] and tau_1(p_1)=[2] start the induction.
Thus the j-color projection is p_(j-1), with trace [j]>0 for ALL j<N.

As a useful endpoint check, p_(N-1) is still definable (its last
denominator is [N-1]>0), but its positive trace is [N]=0. It is therefore
the ZERO operator in this path representation. There is no nonzero
positive projection which may be divided by [N]; the proof explicitly
stops before the Kashaev color.

## 4. Cabling, the retained trace, and framing

For b strands of common ordinary color j let ell=j-1 and put
P=p_ell tensor ... tensor p_ell on b ell fundamental strands.
Its factors commute and are orthogonal projections, so P is one too.
Equation (4) proves exactly

    tau(P)=[j]^b.                                (8)

A positive crossing of two ell-strand blocks is the usual ell^2
fundamental braid word. The Yang--Baxter relation slides every internal
block generator through it, moving the first block's generator to the
second and vice versa. Applying the polynomial recursion (5) proves
that this block crossing interchanges the two p_ell factors and hence
commutes with their product. Its inverse does too. Thus every cabled
colored braid is unitary and preserves P, directly in the positive
path representation. No assertion that the original tensor metric
itself is positive is used.

Let U denote this unitary cabled word. Since the endpoint weight D is
positive and commutes with both U and P, Schatten Cauchy--Schwarz gives

    |tau(PU)|=|Tr(D^(1/2)P U P D^(1/2))|
                  <=Tr(DP)=[j]^b.               (9)

Equivalently restrict to the image of P and sum unitary diagonal
entries with their positive weights. The reduced closure divides by
the retained [j]>0, yielding

    |C_j(q_N)|<=[j]^(b-1), 1<=j<N.              (10)

Here identifying that reduced closure with the original cut is the
separate actual-color comparison, not an extra positivity premise.
The actual zero-framing factor is a power of q^((j^2-1)/2), and all
retained fundamental/color Cartan phases likewise have modulus one.
They do not change (9)--(10). Their exact values are retained in the
comparison audit. At N=2 the only ordinary color is j=1 and C_1=1.

Finally sin(pi/N)>=2/N implies [j]<=sin(pi/N)^(-1)<=(N/2), so for
a fixed b-strand presentation the whole ordinary-color vector has
polynomial size. This conclusion concerns the specific principal root
and the ordinary range; it makes no estimate for j=N.

## 5. Independent checks

[The new audit](../experiments/audit_positive_ordinary_color_path_trace.py)
constructs the path matrices without importing any Jones/trace library.
It checks adjacent relations, noncommuting Markov words, every permitted
projection including j=N-1, the vanishing next projection, disjoint color
traces, cabled-braid preservation and both crossing signs. Whole colored
closures include their zero-framing unit phases. These finite checks
supplement the uniform proofs above and are not a premise for (10).

An additional independent proof reread checked the trace recursion without
semisimplicity, the expanded square calculation in (6), preservation of
the two color projections under block braiding, the j=N-1 endpoint and
the empty-cable N=2 case. It found no substantive gap in this path-algebra
argument. A fresh run of the audit passed; those computations remain
supplementary to the all-level proof, and do not replace the separate
comparison with the original ordinary-color cut.
