# Pointed Steinberg modules and a basis-free pentagon

Research note, 25 October 2026. This develops the algebraic recoupling
theory suggested by the period torsor, rather than another knot case.
Cyclic 6j-symbols already have this origin: Kashaev,
[Quantum Dilogarithm as a 6j-Symbol](https://arxiv.org/abs/hep-th/9411147).
The proofs below are direct; no novelty is claimed for the categorical
pentagon. A particular published matrix normalization is not assumed.

The subsequent [integral extension](cyclic_steinberg_lattice.md)
extends the local algebraic factorization to every level, supplies the
even-level determinant sign, and computes the recoupling lattice at
simultaneous nilpotent degeneration. Its endpoint chain also accounts
for the actual quantum-group Borel coproduct. The odd-level analytic
and global normalization conventions below are not automatically
extended by that local calculation.

## 1. A rigid local vacuum

Fix odd n and a primitive n-th root omega in a characteristic-zero field K.
For t and 1-t nonzero use the split cyclic algebra and module

    A_t=K<X,Y>/(XY=omega YX, X^n=t, Y^n=1-t),
    E_t=K[x]/(x^n-t),
    X f(x)=x f(x), Y f(x)=(1-x)f(omega^(-1)x).

The norm identity in `heisenberg_period_torsor.md` proves the splitting.
Its distinguished vector is the unit 1, since

    (X+Y-1)f=(1-x)[f(omega^(-1)x)-f(x)].                (1.1)

As 1-x is a unit, the kernel is exactly K*1. Therefore X+Y-1 has
rank n-1, and a -> a.1 identifies the pointed module with

    (E_t,1)=(A_t/A_t(X+Y-1),[1]).                      (1.2)

A cyclic-dilogarithm matrix is a change between frames of this algebraic
vacuum, rather than an additional choice of an analytic solution.
Its determinant-normalized frames require the preceding Heisenberg cover.

This module is the local Faddeev difference module itself. In the
previously audited functional equation set

    q=exp(2pi i b^2),
    X=-q^(-1/2)exp(2pi b Z),
    (Y f)(Z)=f(Z-i b),

where q^(-1/2)=exp(-pi i b^2). Then XY=qYX and exactly

    (X+Y-1)Phi_b=0.

For b^2=1/n with odd n, X^n=exp(2pi sqrt(n) Z)=t and the
dual functional equation gives Y^n Phi_b=(1-t)Phi_b. Moreover

    Y[f(X)Phi_b]=(1-X)f(q^(-1)X)Phi_b.

Thus its central fibre is precisely (E_t,1), under f(x) -> f(X)Phi_b.
This identifies the operator, parameter and vacuum, without an
analytic limiting argument. The remaining central period multiplier
is fixed by the exact identity in `rational_quantum_dilogarithm_torsor.md`;
the module relation alone does not determine that multiplier.

## 2. Coproduct and central characters

Use the quantum affine bialgebra

    B=K<X,X^(-1),Y>/(XY=omega YX),
    Delta X=X tensor X,
    Delta Y=X tensor Y+Y tensor 1.

Multiplication verifies the relation after Delta. Both iterated
coproducts send Y to

    X tensor X tensor Y+X tensor Y tensor 1+Y tensor 1 tensor 1,

so Delta is coassociative exactly. The nondegenerate central fibre
X^n=lambda,Y^n=mu is a full n by n matrix algebra after a splitting
extension. The root-of-unity q-binomial identity gives

    (Delta X)^n=lambda_1 lambda_2,
    (Delta Y)^n=mu_1+lambda_1 mu_2.                    (2.1)

This also holds for composite n: the intermediate q-binomial
coefficients vanish because 1-omega^j is nonzero for 0<j<n.
Thus central characters multiply by the affine-group law

    (lambda,mu)*(lambda',mu')
                 =(lambda lambda',mu+lambda mu').

The Steinberg subfamily closes as (s,1-s)*(t,1-t)=(st,1-st).
For it there is a canonical pointed B-linear injection

    m_(s,t):E_(st)->E_s tensor E_t,
    f(x)->f(x_1 x_2).                                  (2.2)

For Y the two terms combine to
[x_1(1-x_2)+(1-x_1)]f(omega^(-1)x_1x_2), proving the assertion.
These maps are strictly coassociative by substitution of x_1x_2x_3.

## 3. A pointed factorization with an explicit ideal certificate

Assume s,t,1-s,1-t,1-st nonzero. In A_s tensor A_t put

    X_tot=X_1 X_2, Y_tot=X_1 Y_2+Y_1,
    Z=Y_1 Y_2^(-1), D=X_1+Z, C=Z X_2,
    tau=(1-st)/(1-t).

The quantum torus relations alone imply

    X_tot Y_tot=omega Y_tot X_tot, DC=omega CD,
    [X_tot,D]=[X_tot,C]=[Y_tot,D]=[Y_tot,C]=0.

Moreover

    X_tot^n=st, Y_tot^n=1-st,
    D^n=tau, (-C)^n=1-tau.                             (3.1)

For the last pair, X_1Z=omega ZX_1, Z^n=(1-s)/(1-t), and
C^n=t(1-s)/(1-t). Oddness gives (-C)^n=-C^n. These exhibit
commuting copies of A_(st), A_tau. Their unital map from the simple
matrix algebra A_(st) tensor A_tau is injective after a splitting
extension and both sides have dimension n^4. The equality descends:

    A_s tensor A_t = A_(st) tensor A_tau.                (3.2)

The vacuum is preserved. Write L_i=X_i+Y_i-1. The exact identities are

    L_tot=X_tot+Y_tot-1=L_1+X_1 L_2,
    L_rel=D-C-1=L_1-Z L_2,                             (3.3)
    L_2=D^(-1)(L_tot-L_rel),
    L_1=L_tot-X_1 D^(-1)(L_tot-L_rel).

Thus the generated left ideals coincide. These identities hold even
at generic quantum parameter in the localized quantum torus; the
root-of-unity equations (3.1) identify its finite central fibres.

There is consequently a unique isomorphism of pointed modules

    C_(s,t):E_(st) tensor E_tau -> E_s tensor E_t,
    C_(s,t)(1 tensor 1)=1 tensor 1,                     (3.4)

intertwining the two commuting algebras (3.2). Explicitly send x^a y^b
to X_tot^a D^b(1 tensor 1). The factorized common vacuum kernel has
dimension one and (3.3) puts the old unit in it. Simplicity and equal
dimensions give invertibility; the unit fixes the scalar.

This is a uniform statement about pointed modules, stronger than the
existence of an unpointed intertwiner. It is not yet an identification
of the global knot period across arbitrary triangulations.

### 3.1 The exact kernel and its normalization unit

This factorization has an explicit finite-product kernel. In the
commutative coordinate algebra E_s tensor E_t write w=x_1x_2, z=x_2.
Then

    D f(w,z)=(w/z)f(w,z)
              +(1-w/z)/(1-omega z)*f(w,omega z).

Induction, starting with f=1, gives

    D^b 1=product_(j=1)^b (1-omega^j w)/(1-omega^j z).

Thus, in the monomial bases, the pointed Clebsch--Gordan map is

    C_(s,t)(u^a v^b)
         =w^a (omega w;omega)_b/(omega z;omega)_b.      (3.5)

No undetermined scalar remains. These are q-factorial ratios in the
same local family as the earlier custom products, now with a specified
module meaning, phase, and vacuum. Taking their magnitudes does not
identify the entire earlier positive state with this tensor construction.

Its determinant also has a uniform formula:

    det C_(s,t)
       =[t(1-st)/(1-t)^2]^(n(n-1)/2).                 (3.6)

Here the target basis is x_1^i x_2^j and the source is u^a v^b, with
the first index ordered first in both. To prove (3.6), first replace
the target basis by w^a z^k. Its determinant is t^(n(n-1)/2): for
each a, reducing z^(a+k) modulo z^n=t contributes t^a; its cyclic
permutation has sign one for odd n.

Over K(w), each column b of (3.5) is multiplied by
N_b(w)=product_(j=1)^b(1-omega^j w). Its field norm is (1-st)^b.
The product of these norms is (1-st)^(n(n-1)/2).

The remaining columns are R_b(z)=1/(omega z;omega)_b. For b>=1,

    R_b(z)=product_(j=b+1)^n(1-omega^j z)/(1-t).

Their degrees are n-b, while R_0=1. The triangular leading-coefficient
calculation gives

    det(R_b in the z^k basis)
       =omega^[n(n^2-1)/3]/(1-t)^(n-1).

The sign is one because its exponent is (n-1)^2. This determinant
appears to the n-th power over K, so its phase disappears exactly.
Combining the three factors proves (3.6).

Writing h=(n-1)/2 and f=t(1-st)/(1-t)^2, a specified cyclic
determinant normalization can be taken on the mu_n-cover

    gamma^n=f^(-h), C_normalized=gamma C_(s,t).          (3.7)

It has determinant one because dim C=n^2 and det C=f^(nh).
Equation (3.7) specifies a particular mu_n subcover of the general
mu_(n^2) determinant choices. It retains a nonconstant algebraic unit,
not just an unspecified root-of-unity scalar. Compositions must carry
this unit before any peripheral specialization.

For fixed nondegenerate classical parameters this normalization also
has a uniform size bound, with no choice of root affecting it:

    log|gamma|=-(n-1)/(2n)*log|f|.

Thus any fixed finite recoupling diagram accumulates a bounded
logarithmic contribution from these units as n varies. Self-dual
finite Fourier measures add only explicit powers of n. After the
states and their period classes are identified, these recorded
changes cannot alter their exponential volume rate. This assertion
applies at nonzero finite f; cancellation and specialization at a
zero or pole must be performed in the generic period identity first.

## 4. Recoupling without integral limits or chosen matrices

For arbitrary nondegenerate affine central characters g,h,gh, take
splitting modules H_g,H_h,H_(gh) of dimension n and define

    W(g,h)=Hom_B(H_(gh),H_g tensor H_h).

The tensor product is an n^2-dimensional module over the split matrix
algebra of the product character, hence n copies of its n-dimensional
irreducible module. Therefore dim W(g,h)=n and evaluation is an isomorphism

    W(g,h) tensor H_(gh) -> H_g tensor H_h.              (4.1)

This only uses the specified nondegenerate central fibre, not a
semisimplicity assertion for all B-modules.

For three characters composition gives two canonical isomorphisms

    W(g,h) tensor W(gh,k)
       -> Hom_B(H_(ghk),H_g tensor H_h tensor H_k),
    W(h,k) tensor W(g,hk)
       -> Hom_B(H_(ghk),H_g tensor H_h tensor H_k).

Their ratio defines the basis-free recoupling map. For four characters
every parenthesization identifies in the same way with

    Hom_B(H_(ghkl),H_g tensor H_h tensor H_k tensor H_l).

Both compositions in the pentagon are the same map through this
common space. This proves the pentagon exactly by coassociativity
and composition. It requires neither analytic limits nor a choice
of cyclic-dilogarithm branches.

On the Steinberg subfamily W(s,t) is canonically a pointed Steinberg
module E_tau: the commuting algebra of Section 3 acts by
postcomposition and its distinguished vector is m_(s,t). Equations
(3.3) put it in the relative vacuum line. This identifies (3.4) with
the evaluation map (4.1).

Choosing bases turns these recoupling maps into cyclic 6j matrices.
Frames introduce exactly the factors and root choices that require
normalization torsors. Literal equality to a particular matrix still
requires its basis, roots, measure and determinant convention to match.

## 5. The global comparison that remains

This supplies one uniform algebraic origin of the local 2--3
recoupling relation on the nondegenerate locus at every odd level.
Individual knot integrals need not reprove this coherence statement.

The finite face theorem evaluates singular presentations and edge
reduction supplies the boundary module. The required intrinsic knot
period still needs a functorial gluing construction joining these
pieces, with its peripheral data, duality pairings and normalization
line. Degenerate central fibres are not covered by the matrix-algebra
argument and must be handled explicitly in that construction.

The rational Faddeev identity fixes its local Heisenberg/dilogarithm
period. Its global cycle and the regulator comparison remain separate
obligations. Coassociativity proves coherence, but does not by itself
prove the numerical volume-growth law. The next task is this global
comparison, not more knot cases.
