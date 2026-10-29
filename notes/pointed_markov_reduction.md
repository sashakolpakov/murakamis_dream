# Markov reduction of the actual source and its geometric determinant line

Research note, 26 October 2026. This continues the invariant's own
quantum A/torsor program. The source is the original reduced
Kashaev/ADO cut. No comparison with Jones, a custom state, or a
published regulator theorem is used. We prove an exact finite
source contraction, a uniform geometric Gaussian reduction, and
explicit Markov chain equivalences for the linearized holonomy
complex. The selected global period's volume norm remains unproved.

**Uniform compatibility theorem.** Let beta be any braid whose
closure is a knot, at any N>=2 with the original quantum cut
normalization. For either Markov stabilization:

1. The actual finite cut contracts exactly to the old cut as
   a whole meridian germ, with its full modified dimension.
2. At every nondegenerate geometric critical chart, the added
   quadratic period complex is the old complex plus one
   explicit acyclic rank-one pair. Its variable principal
   amplitude cancels the determinant of that pair.
3. At every irreducible fixed-trace representation with
   ker(dF-I) equal to the infinitesimal conjugation orbit,
   the linearized holonomy complex is the old one plus an
   explicit acyclic rank-two pair, and its torsion is
   unchanged. It is also invariant under braid conjugation
   and braid relations.

The proof below has arbitrary N, braid and representation.
The finite computations in the audit validate the formulas;
they are not the proof or an assumption on knot examples.
This is a uniform structural lemma for the intended volume
theorem, not the volume theorem itself.

## 1. The full finite source has an exact contraction

Use q=exp(pi i/N), Q=q^2, x=-M/q, the original checked
crossings B_+,B_-=B_+^(-1), pivot g=K^(1-N), and
theta=x^(1-N). For every N>=2 and every whole color germ,

    ptr_g(B_+)=theta I,
    ptr_g(B_-)=theta^(-1)I.                       (1.1)

Thus the zero-framed Markov contraction is identity. The
full modified dimension d_N(M) on the remaining cut is
unchanged; no peripheral factor is evaluated separately.

Here is a coefficient proof, in the original finite basis.
It uses the independently derived coefficients in
[the actual crossing note](relative_octahedral_period.md#1-exact-formulas-for-both-actual-crossings).
Integer-index conservation makes either partial trace
diagonal. For the positive crossing, write k=a-b. Its
diagonal entry divided by theta is

    x^(-2a) Q^(a(a-1))
       sum_(k=0)^a (-1)^k Q^(k(k-1)/2+(1-a)k)
                      {a choose k}_Q (t;Q)_k,
    t=Q^(1-a)x^2.                                (1.2)

The sum equals t^a. To prove this, expand t^a in the
Newton basis P_k=(t;Q)_k and use
t P_k=Q^(-k)(P_k-P_(k+1)). Induction and the Gaussian
binomial recursion give precisely the coefficients in
(1.2). Its prefactor cancels t^a, proving the first identity.

For the negative crossing put n=N-1-a. Root reflection gives

    {a+k choose k}_Q
       =(-1)^k Q^(ak+k(k+1)/2){n choose k}_Q.

Invert the k Pochhammer factors. With w=Q^a x^(-2),
the remaining diagonal sum becomes

    x^(2a+1-N) Q^(-a(a+1))
               sum_(k=0)^n {n choose k}_Q w^(-k)(w;Q)_k.

The last sum is w^(-n). Equivalently,
sum_k {n choose k}_Q w^(n-k)(w;Q)_k=1; induction follows
from {n+1 choose k}_Q=Q^k{n choose k}_Q+{n choose k-1}_Q
and P_(k+1)=(1-wQ^k)P_k. The x exponent is then N-1
and the remaining Q exponent is -aN. This proves the
second identity in (1.1), for the whole meridian function.

## 2. The regular geometric contraction has one critical variable

Use the actual balanced coefficients, with position variables
A,B, transfer C and Y=M^2, as in
[the principal density calculation](actual_cut_residue_and_principal_density.md).
Closing the added strand imposes

    B=A/C for B_+,
    B=AC  for B_-.

The original internal shift ratios give the respective
stationary multipliers

    R_+=-(1-YC/A)(1-B)/[B(1-C)],
    R_-=(1-AC)(1-Y/B)/[A(1-C)].

On the nondegenerate chart R_sign=1 has the unique solution

    D=1+Y-A,
    C_+=A D/Y, C_-=Y/(A D),
    B_+=B_-=Y/D.                                (2.1)

The excluded factors are actual chart divisors, including
A=1,Y and D=0; they are not deleted from the quantum source.

Let c=Log C and hold a=Log A fixed. The trace-phase Hessian
in its single remaining internal variable is

    h_+=D^2/[(A-1)(A-Y)], h_-=-h_+.              (2.2)

These follow by taking (0,-1,1) and (0,1,1) directional
derivatives in (Log A,Log B,Log C) of the actual phase Hessian.
They are units on the stated regular chart.

The original principal amplitudes include their closing pivot
and zero-framing factors. Their squares are

    b_+^2=a_+^2/B^2,
    b_-^2=Y^2 a_-^2/B^2.

Substitution of (2.1) gives exactly

    b_+^2=h_+, b_-^2=h_-,
    b_sign^2/(-h_sign)=-1.                       (2.3)

Thus all input- and meridian-dependent factors cancel from
the one-variable Gaussian contraction. The remaining minus
sign belongs to the fixed Gaussian/quantum normalization
line; it is not a new adjustable peripheral multiplier.
The full finite normalization is fixed by (1.1). We retain
that line rather than evaluating an infinite compact product
at a root of unity.

The cut-momentum and meridian character multipliers both
equal one at (2.1). This follows by multiplying the two
input shift ratios for the former and substituting in the
actual meridian half-step ratio for the latter. Locally the
critical phase therefore differs by a base-only term and
integer stationary windings. Those windings are retained
characters equal to one on the actual integer lattice.
The base-only term has its specified original normalization.

## 3. An explicit map on the quadratic period complexes

Let X be the old phase coordinates and let v be the column
derivative of c_sign(A(X),Y). For a fixed meridian,

    partial_(Log A)c_sign
               =sign*(1+Y-2A)/D.

After the stated integer flattening, the critical added phase
has no X-dependent value. Its Hessian adjoining the old
quadratic form H is consequently

    H_new=[H+h v v^t  -h v; -h v^t  h].           (3.1)

The unit-determinant change c_tilde=c-c_sign(X) gives

    U=[I 0;v^t 1],
    U^t H_new U=diag(H,h).                       (3.2)

This is a chain equivalence of the two-term quadratic
complexes. It identifies the old kernel with the graph
(xi,v^t xi) and adds the acyclic pair [k --h--> k].
The determinant factor is h. Equation (2.3) supplies its
actual amplitude correction, including the universal sign.

This proves stabilization compatibility of the variable
geometric normal determinant line for every regular
irreducible critical representation. It is not a claim that
the selected global relative cycle has already been pushed
through an arbitrary pole divisor.

## 4. Markov chain equivalences for the holonomy complex

We can now prove that the finite-dimensional scalar in the
[density note, equation (6.4)](actual_cut_residue_and_principal_density.md#an-invariant-finite-dimensional-complex-for-the-reduction)
is invariant under Markov moves on its regular locus.

Let X be the product of the noncentral fixed-trace meridian
classes. At an irreducible fixed point H of the Hurwitz
map F, use

    0 -> sl_2 --a--> T_H X --(dF-I)--> T_H X
                                      --m--> sl_2 -> 0,
    a(xi)=([xi,H_j])_j,
    m(V)=dP(V)P^(-1), P=H_b...H_1.               (4.1)

It is acyclic when ker(dF-I)=im a. The earlier note proves
injectivity of a, surjectivity of m and the well-defined
torsion T_beta=det[a,V]/det[(dF-I)V,W], mW=I.

For stabilization put A=H_b and append a new meridian Z.
Writing G=F(H), the two extended maps are

    F_+(H,Z)=(G_<b, G_b^(-1) Z G_b, G_b),
    F_-(H,Z)=(G_<b, Z, Z G_b Z^(-1)).

Their fixed-point schemes are exactly F(H)=H,Z=H_b.
This follows by eliminating Z directly and holds over
Artin rings, not just on reduced points.

At such a point write w=(dF(V))_b and use the domain
coordinate u=z-w. In the output use

    V'_b=V_b+Ad_(A^(-1)) z, V'_<b=V_<b,

keeping the new last coordinate z. Both are triangular
changes of determinant one. The middle differential becomes

    diag(dF-I,-I)                   for F_+,
    diag(dF-I,-Ad_A|_(T_A orbit))   for F_-.       (4.2)

The infinitesimal conjugation maps to (a,0). The extended
product is P_new=Z P, and its transformed last map is

    m_new(V',z)=Ad_A m(V').                      (4.3)

Indeed the z term in d(ZP)(ZP)^(-1) cancels precisely
against the correction in V'_b. Equations (4.2)--(4.3)
are an explicit chain equivalence with the old complex
and one acyclic two-dimensional pair. Both Ad_A on sl_2
and Ad_A on its tangent conjugacy orbit have determinant
one; the latter also follows from invariance of dK wedge
de/e. The signs in -I have even dimension. Therefore

    T_(beta stabilized)(H,H_b)=T_beta(H)          (4.4)

for either sign, and regularity is preserved.

Braid conjugation is also a chain equivalence: a Hurwitz
coordinate change is equivariant and preserves P. Its
derivative changes both middle bases equally, so the torsion
ratio is unchanged. Braid relations are identities of the
Hurwitz maps. Thus this scalar is invariant under the
braid presentation moves, with its meridian trace and
irreducible representation marked. No equality with a
separately defined Reidemeister torsion is used or asserted.

## 5. Consequence for the actual A/torsor program

The actual finite source contraction, its geometric Gaussian
pair, and the holonomy deformation complex now all have
explicit stabilization maps. This is a compatibility for
structures attached to the same invariant. It avoids assuming
that two arbitrary periods with the same A-symbol coincide.

The subsequent [uniform principal-density proof](quantum_source_bridge_extension.md)
now compares the variable Gaussian determinant line with (4.1),
including its kernel, cut co-source and explicit presentation-parity
character. The base-only quantum normalization line and transport
of the selected global relative period remain separate.
These local contractions do not prove that its
geometric block survives with subexponential comparison
factor across levels. That norm statement is still the
required volume theorem.

[Audit](../experiments/audit_pointed_markov_reduction.py).
[Results](../experiments/pointed_markov_reduction_results.json).
