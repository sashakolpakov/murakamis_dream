# Pointed recoupling and relative period descent

Research note, 25 October 2026. This continues the structural program.
The result is an exact comparison of selected algebraic vacua, their
normalization lines and their classical Bloch labels under recoupling.
It applies uniformly to finite recoupling diagrams. The remaining
identification with the intrinsic knot period is stated in Section 7.

Write C_(s,t) for the explicit pointed factorization in
`pointed_steinberg_recoupling.md`, and set

    tau(s,t)=(1-st)/(1-t),
    f(s,t)=t(1-st)/(1-t)^2,
    h=(n-1)/2,
    det C_(s,t)=f(s,t)^(nh).

All formulae are on the nondegenerate parameter locus. Local maps are
defined over its algebraic function field and extend wherever their
intrinsic sections are regular. No angle-positivity assumption is used.

## 1. The pointing extends to arbitrary matched affine transports

The Steinberg family is a normalization of a larger pointed family.
Let g=(lambda,mu) be an affine central character with lambda*mu nonzero.
Choose nonzero endpoint roots a,b such that

    b^n=lambda*a^n+mu.

On E_(g;a,b)=K[x]/(x^n-lambda), define

    X f=x f, Y f=(b-a x)f(omega^(-1)x).

The norm is b^n-a^n*lambda=mu. The unit is the unique vacuum line
for Y+aX-b, since this operator is
(b-a x)(sigma^(-1)-1). Rescaling X'=aX/b,Y'=Y/b gives exactly
the Steinberg module with parameter lambda*a^n/b^n.

For g,h use endpoints c->d and a->c, respectively. Assume also
mu_(gh)=mu_g+lambda_g*mu_h is nonzero, so that the composite and relative
matrix algebras below are nondegenerate. The tensor coproduct preserves
the pointing of their composite a->d:

    L_tot=L_g+X_1 L_h,
    f(x) -> f(x_1x_2).

This follows from c matching on the two factors. The injections are
strictly coassociative. Thus the pointed construction is not confined
to affine characters fixing the point one.

The same relative operators Z=Y_1Y_2^(-1), D=X_1+Z, C=ZX_2 have
central character

    lambda_rel=mu_(gh)/mu_h,
    mu_rel=-mu_g*lambda_h/mu_h.

Their compatible endpoints are c/a -> d/a. With L_rel=-C+(c/a)D-d/a,

    L_tot=L_g+X_1 L_h,
    L_rel=(L_g-Z L_h)/a,
    L_h=D^(-1)(L_tot-a L_rel).                          (1.1)

These are exact identities at indeterminate quantum parameter.
Normalizing the two endpoint modules gives the earlier C_(s,t), with
s=lambda_g*c^n/d^n and t=lambda_h*a^n/c^n. The resulting factorization
therefore preserves the selected unit, with all endpoint scalars known.

For the unscaled monomial bases its determinant is

    [a^n*lambda_h*mu_(gh)/mu_h^2]^(nh).                 (1.2)

Indeed the target basis rescaling has determinant (a/d)^(n^2 h),
the source rescaling has determinant (ac/d^2)^(n^2 h), and
f(s,t)=lambda_h*mu_(gh)*(ac/d)^n/mu_h^2. Substitution in the
previous determinant formula gives (1.2).

## 2. The Racah map is the same explicit pointed factorization

Consider three Steinberg modules E_r tensor E_s tensor E_t, with
all nonempty consecutive products different from zero and one. Put

    a=tau(rs,t), b=tau(r,s),
    c=tau(r,st), d=tau(s,t).

Then cd=a and tau(c,d)=b. Order the left decomposition as
E_(rst) tensor E_a tensor E_b, and the right as
E_(rst) tensor E_c tensor E_d. Their evaluation maps are

    I_L=(C_(r,s) tensor 1) P_23 (C_(rs,t) tensor 1),
    I_R=(1 tensor C_(s,t)) (C_(r,st) tensor 1).

Here P_23 is the literal vector-space permutation. Exactly

    I_L=I_R (1 tensor C_(c,d)).                         (2.1)

In particular the recoupling maps the product of the two distinguished
multiplicity vacua to their product, with coefficient one.

For a proof uniform in the quantum parameter, write

    Y_12=X_1Y_2+Y_1, Y_23=X_2Y_3+Y_2,
    Y_123=X_1X_2Y_3+X_1Y_2+Y_1.

The two left relative pairs A,B and two right pairs C,D have

    X_A=Y_123 Y_3^(-1), X_B=Y_12 Y_2^(-1),
    X_C=Y_123 Y_23^(-1), X_D=Y_23 Y_3^(-1),
    Y_A=-Y_12 Y_3^(-1)X_3, Y_B=-Y_1Y_2^(-1)X_2,
    Y_C=-Y_1Y_23^(-1)X_2X_3, Y_D=-Y_2Y_3^(-1)X_3.

Keeping these orders, direct multiplication gives

    X_A=X_C X_D, Y_A=X_C Y_D+Y_C,
    X_B=X_C+Y_CY_D^(-1), Y_B=-Y_CY_D^(-1)X_D.           (2.2)

For the first identity the intermediate Y_23 cancels. For the third,
1+X_2Y_3Y_2^(-1)=Y_23Y_2^(-1); the others follow by the same
ordered products. These are exactly the two-factor factorization
formulae of C_(c,d). Both sides of (2.1) preserve the unit in all
three factors and intertwine the same full matrix algebra. The
pointed uniqueness theorem proves equality, including its scalar.

This identifies a recoupling operator with the explicit q-factorial
kernel, rather than only defining it as a ratio of unspecified maps.

## 3. The normalization cocycle and the permutation sign

The units obey the rational identity

    f(c,d)=-f(r,s)f(rs,t)/[f(r,st)f(s,t)].              (3.1)

Let gamma_(s,t)^n=f(s,t)^(-h), so gamma C has determinant one.
Put Gamma_L=gamma_(r,s)gamma_(rs,t) and
Gamma_R=gamma_(r,st)gamma_(s,t). The recoupling from these normalized
tree evaluations is exactly

    F_hat=(Gamma_L/Gamma_R) C_(c,d).                   (3.2)

Its determinant is (-1)^h, not necessarily one. This is forced by
the single permutation P_23 in (2.1): the flip on two n-dimensional
factors, and its tensor extension, both have determinant (-1)^h
for odd n. Dropping that sign would give a false normalization law.

If one independently normalizes C_(c,d) by gamma_(c,d), the ratio
epsilon=Gamma_L/[Gamma_R*gamma_(c,d)] satisfies

    epsilon^n=(-1)^h.

For a Racah normalization with its correct signed determinant, take
eta_(c,d)^n=(-1)^h*f(c,d)^(-h). Then

    Gamma_L/[Gamma_R*eta_(c,d)] is mu_n-valued.          (3.3)

It is constant on each irreducible lifted parameter component.
This proves the rigidity statement with its actual hypotheses and
records the root phase, rather than canceling it at a special value.

## 4. Descent of the selected finite period on a recoupling diagram

For any binary tree T, iterating the pointed C maps gives an
evaluation I_T into the same tensor product of leaf modules. It is
invertible and takes the product vacuum to the product vacuum.
For two trees the transition is I_(T')^(-1)I_T. Consequently

    F_(T',T'') F_(T,T')=F_(T,T''),

and every loop is the identity. This proves exact pointed coherence,
including the pentagon and disjoint recouplings.

If the node maps are multiplied by their specified roots gamma, let
Gamma_T be their product. The transition becomes

    F_hat_(T,T')=(Gamma_T/Gamma_(T'))F_(T,T').            (4.1)

All higher coherence still holds by cancellation. The normalized
product vacuum is transported with precisely this scalar. Thus the
selected line, not just the unpointed module, descends on this
recoupling groupoid with its normalization line.

The conclusion is stable under every finite exterior contraction:
a matrix identity may be tensored with any exterior tensors and
paired along any chosen indices, retaining the same scalar. Sums
are finite, so no face-rank or convergence assumption enters this
step. It includes scalar periods and open boundary tensors, and
does not require the resulting period to be nonzero.

These are algebraic identities on their common parameter cover.
They extend to every regular specialization of the corresponding
sections. Generic units must first be retained and canceled in
that identity; specializing a displayed fraction at a pole is not
a definition of its section.

## 5. The Bloch label is the tetrahedral cross-ratio

For the four cumulative points

    p_0=1, p_1=r, p_2=rs, p_3=rst,

the cross-ratio in the recorded convention is

    z(r,s,t)=(1-rs)(1-st)/[(1-rst)(1-s)]
              =b/c=tau(c,d)/c.                        (5.1)

Thus the recoupling has a natural tetrahedral Bloch label. Four
consecutive parameters give five cumulative points; their alternating
tetrahedral boundary is

    [z(s,t,u)]-[z(rs,t,u)]+[z(r,st,u)]
                         -[z(r,s,tu)]+[z(r,s,t)]=0.    (5.2)

This is the same five-point relation established in the Bloch note,
by deleting each of the five vertices. The classical regulator and
the quantum pointed recoupling therefore have compatible local
coherence diagrams. Equating their *global period classes* still
requires the comparison in Section 7.

## 6. Intrinsic normalization lines from spinor brackets

The extra affine-frame data in f must be distinguished from the
cross-ratio (5.1). For four nonzero affine coordinates p_i, direct
substitution gives the Racah unit

    f_R=-p_1p_2(p_0-p_2)(p_1-p_3)
                  /[p_0p_3(p_1-p_2)^2].              (6.1)

Choose nonzero homogeneous flag vectors v_i in K^2, and set
lambda_ij=det(v_i,v_j). In the affine frame v_i=(p_i,1), remove
the displayed vertex-frame factor to obtain

    f_bar=-lambda_02 lambda_13/lambda_12^2.             (6.2)

This is GL(2)-invariant. Under v_i -> a_i v_i it is multiplied by
a_0a_3/(a_1a_2), so it is intrinsically a section of a decoration
line, rather than an invariant number after forgetting those lines.
The cross-ratio and its complement are

    z=lambda_02 lambda_13/(lambda_03 lambda_12),
    1-z=-lambda_01 lambda_23/(lambda_03 lambda_12),

by the elementary Plucker relation. Their n-th roots give the local
Fermat norm cover on this flag torsor.

There is also an exact shared-face normalization. On an ordered
triangle put

    q_ijk=lambda_ik/lambda_jk^2.

With the usual multiplicative coboundary,

    f_bar(0123)=-(delta q)(0123)^(-1).                  (6.3)

Choose roots alpha_ijk^n=q_ijk^h on faces and define the tetrahedral
root eta_0123=(delta alpha)(0123). Then

    eta_0123^n=(-1)^h*f_bar(0123)^(-h),                 (6.4)

the signed Racah normalization of Section 3. Sharing the face roots,
rather than choosing unrelated tetrahedral roots, makes their product
over a 3-chain equal to the face product over its boundary. Interior
face roots cancel. On the boundary of a 4-simplex it is one because
delta^2=1. This proves strict compatibility of these scalar
normalization sections with the five-term relation.

The statement is valid for actual equivariant vector flags or for
sections of their decoration lines with the corresponding transition
functions. A PSL(2) lifting obstruction or nontrivial peripheral
characters must remain in those line transitions; they are not set
to one by choosing an affine chart. Such data can leave peripheral
factors after gluing, exactly where a generic unit can specialize
to a numerical multiplier.

## 7. The remaining global theorem

We have proved selected-vacuum coherence on the recoupling parameter
groupoid, algebraic transport through arbitrary finite exterior
contractions, and relative descent of its normalization line on
decorated flag charts. The local Bloch label has the same five-point
coherence. These statements are uniform and use no knot census.

The subsequent `affine_frame_period_transport.md` and
`projective_frame_period_torsor.md` prove full matrix/frame covariance
on the specified local root covers. They also prove that the selected
unit must generally be transported to a nonconstant vector. A global
knot period still needs an intrinsic decorated-character gluing
construction, its peripheral lifts and its selected period class matched
with the literature state. The exact local Faddeev comparison does not
by itself identify that global cycle. The regulator comparison across
levels also remains necessary for the volume conjecture.
