# Independent audit of the Fourier partial geometric-support theorem

27 October 2026. Proof pass of Section 7 of
[the partial-support theorem](partial_geometric_support_theorem.md),
with the source category and normalization checked against
[the whole wire polarization](actual_two_cut_fourier_polarization_and_cap.md)
and [the actual Fourier normal block](actual_fourier_polarized_geometric_normal_block.md).
The new result is an operator for an actual all-level ROOT partial
family, with a nonzero formal geometric line. It is not an operator
identity for the whole generic-q Vandermonde germ or a theorem about
the final selected geometric coefficient.

## 1. The actual raw source retains both factors of 1/N

The literal partial trace on the second wire is invariant under
I tensor V, retaining the first original rank-one row. Thus

\[
 \widetilde F_N(a,j)=\sum_c T^V_{c,j;a,j}
      =\frac1N\sum_{b,\nu,u}Q_N^{j\nu}W_N(a,b,\nu,u),
 \qquad F_N=\frac1N\sum_{a,j}\widetilde F_N(a,j).
\]

The inner 1/N is the Fourier inverse and the outer 1/N is the
original first-cut source. Charge conservation changes the first
output to a-nu, but does not impose nu=0 before transforming.
Summing j afterward kills exactly the nonzero offsets in their
actual range |nu| less than N. The four original head bounds and
original pivots stay in W_N; no new second pivot occurs. Restricting
c=a early would make the transformed diagonal independent of j and
would destroy this construction.

The generic-q Vandermonde inverse is the Lagrange coefficient matrix,
not Q^(-bj)/N. The proper lift used in the certificate is the latter
monomial kernel. They agree at every original root for every M,
which is sufficient for its all-level ROOT meridian identity. Their
q-normal derivatives generally differ. The theorem states this
distinction rather than suppressing the actual connection or carries.

## 2. The nonzero certificate survives its new dimensions and boundaries

Opening the two physical cuts adds one independent integer boundary
offset on the integral tree flow chart. After polarization the internal
labels are b,nu,u, of dimension r_F=m+1; a and j remain external.
All positions, transfers and factorial lengths are fixed integral
affine forms in these variables and N. The additional factor
q^(2j nu) has a rational proper ratio under every internal shift.
Its external multiplication character is q^j; the possible q square
roots and existing signs remain on their stated covers.

The Section 2 count therefore has r_F+4 multiplication variables,
including x,z=q^N,q^a,q^j. Its image space is O(R^(r_F+4)), while
the independent Ore monomials including the meridian and r_F internal
shifts number (R+1)^(r_F+5). The boundary count also extends: if
near-boundary linear forms have rank c on N,a,j,b,nu,u, their labels
have O(R^c) possibilities and their c binomial reductions remove
the same c multiplication degrees. No external label is silently
treated as fixed during that count.

A strict cone exists by taking the old transfer variables small and
positive and the cut positions away from both endpoints. The tree
particular open flow changes all these finitely many affine forms
by fixed multiples of nu; a sufficiently smaller two-sided nu
interval preserves strict inequalities. The Fourier index j has its
own independent interior interval. Thus the open identity extends
to the independent character field by the same cone-density proof;
it is not an identity known only at one discrete frame.

The factor 1/N is a common line fixed by all relevant shifts and
does not affect the dimension count. Strip the largest common z+1
factor from the WHOLE finite-array certificate before evaluating
z=-1. Finite original head factorial denominators remain regular
at q_N. Least-degree expansion in the internal shifts around one
then produces a nonzero meridian operator after exact finite moment
extraction. Every actual zero-extension stratum is included. There
is no multiplication by an independently supplied geometric factor.

## 3. The formal geometric block is supplied by the actual open phase

The entire open coefficient, with its original finite factorial
arguments, gives S_open, not just a list of fixed-band ratios. The
new Fourier monomial gives the exact additional phase vt. Fixing the
old first physical position leaves one old framing radical xi in
the (b,u) variables. The old Hessian has precisely that radical.
The mixed derivative c satisfies c dot xi=d log p_e(xi). This is
nonzero on the new regular polarization chart. Hence

\[
 H_{new}=\begin{pmatrix}H_0&c\\c^t&\gamma\end{pmatrix}
\]

has zero kernel: pairing its first equation with xi kills the last
coordinate, then the remaining vector is a multiple of xi, and the
last equation kills that multiple. This argument is valid even at
an old two-position projection caustic. It assumes the original
regular coefficient-shape chart, as stated.

The birational (A,p_e) assertion at a complete discrete-faithful
point also passes. An upper triangular word in the discrete torsion
free projective group has equal diagonal entries: contracting or
recurrent conjugates of the cut parabolic otherwise contradict
discreteness, and a nontrivial finite diagonal ratio gives torsion.
If p_e were independent of the remaining frame coordinate, the
prefix Mobius formula would force U-V=b E_12 and both U,V upper
triangular. Their equal-diagonal property would then make the
second position independent too, contradicting the chosen pair.
The displayed rational inverse consequently defines a nonempty
birational chart. This is not a global compactification assertion.

At the selected incidence v=-Log p_e, the new critical point has
t=0 and value S_geo. The Fourier character is one there, the
original leading amplitude is a unit, and the new Hessian is
invertible. There is therefore a nonzero formal Gaussian block
with the original regulator action. The normalized Fourier pair
has (1/N)H_N^(-2)=1/(2 pi i H_N). Its ordered cross-pair phase is
explicitly fixed; it does not hide a variable source factor.

This argument permits macroscopic nu as an actual proper-array
coordinate before contraction. It does NOT sum a fixed-offset
asymptotic formula over offsets growing with N.

## 4. Why the SAME operator acquires the geometric factor

The auxiliary coefficient realization has the exact proper ratios
used by the finite certificate. Translating every nondegenerate
internal formal integration coordinate gives the exact exponential
weight character. Applying the SAME least-moment extraction to that
identity therefore makes the finite-array operator annihilate the
nonzero formal block. No unsummed framing radical or omitted Green
endpoint is used in this step: both framing coordinates are external
in the Fourier partial family.

For a fixed external cut position and Fourier character, its critical
value remains S_geo throughout the meridian deformation germ. The
geometric point stays at t=0 and the other critical equations hold;
the derivative at fixed external labels is the preferred longitude
derivative. Thus its first meridian shift ratio is L_geo. Strip the
operator's common scalar q-1 valuation. Its first nonzero classical
symbol vanishes on L_geo for independent external framing characters,
so the marked irreducible A_geo divides it over their transcendental
coefficient field. Formal Ore right division gives the stated line
quotient as well. Positive shift order follows from the nonzero block;
an order-zero nonzero multiplier cannot annihilate it.

The geometric factor is consequently forced by a nonzero operator
constructed from the actual finite family, rather than appended to
an unrelated annihilator. The proof does not identify the minimal
full scalar operator, and the factor may be lost in the final
source-paired sum over a,j. The complete peripheral line is still
transported by its ordered Ore gauge.

## 5. Independent check of the whole wire map and bounded-test formula

The Lagrange inverse, both truncated-shift carries and the actual
Ecal,F,K transforms in the whole polarization note pass algebraically.
In particular their endpoint terms have coefficients 1-Q^N and
M-M inverse separately. The derivative connection
A_Q=(D_Q V)V inverse=J_eval(V J V inverse) has the displayed order;
the resulting commutator drops out only after the actual partial
trace. Its root norm bound (N-1)^2 follows from V/sqrt(N) unitary.

For the independent bounded-band theorem, implicit differentiation
gives u prime=-S_uu inverse S_u nu. Differentiating the determinant
of the Hessian gives exactly the stated alpha, and differentiating
the critical action gives beta=(S_nu nu-ell_i G^ij ell_j)/2.
The first Gaussian correction cancels in Z_q/Z_0 at order H.
Formal constant-term integration by parts then produces
-alpha E_eta h+beta E_eta squared h with the printed signs.
These finite tests keep physical B and Fourier eta independent.
They are consistent with, but are not used as a substitute for,
the macroscopic open-phase proof in Sections 2--4 above.
