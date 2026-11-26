# The selected geometric factor in an actual all-level annihilator

1 November 2026. Private theorem and dependency audit.

The new marked representation construction identifies the entire
characteristic germ selected by the microscopic invariant, for the
all-circle classes below. This is stronger than agreement of a cusp
tangent. It gives divisibility by one geometric irreducible factor.
It does not give equality with the full classical A-polynomial or an
equality of quantum operator ideals.

## 1. Precise statement and conventions

Let \(K\) admit an original ordered all-circle tree presentation with
at least one edge, one main knot component, and no additional component
closed inside a tangle. Keep the actual endpoint orders, orientations,
primitive crossing-circle slopes and preferred knot longitude.
Write \(d_v\) for the degree of a circle vertex and
\[
 n_v=\epsilon_v-2p_v,\qquad \epsilon_v\in\{-1,0,1\}.
 \tag{1}
\]
Assume one of the already proved finite-source hypotheses:

* the fixed signed powers are independently sufficiently long for the
  original strict-tree theorem;
* \(\sum_v d_v/(d_v^2+n_v^2)\le2^{-25}\);
* \(\max_v d_v/(d_v^2+n_v^2)\le2^{-120}\).

The last two alternatives need not have every \(n_v\ne0\).
The tree, powers and actual knot are fixed before the level tends to
infinity. Both level parities are included. All original knot-pattern
qualifications are retained; in the two-circle case the excluded
two-odd pattern is a link, so the knot case includes a pure leaf.

Let \(F_N(M)\) be the actual zero-framed reduced ADO state, with
\[
 q_N=e^{\pi i/N},\qquad M=-q_Nx,\qquad F_N(1)=K_N.
 \tag{2}
\]
Thus the marked complete point is \(M=1\), not the raw highest-weight
coordinate \(x=1\). Let
\[
 P(q,M,T)=\sum_{j=0}^{d}a_j(q,M)T^j,\qquad TM=qMT,
 \tag{3}
\]
be a nonzero fixed rational-coefficient operator annihilating the
whole function \(F_N(M)\) for every sufficiently large \(N\).
The coefficients belong to \(\mathbb C(q,M)\); a rational coefficient
field is addressed in Section 6. The operator is an actual all-level
annihilator, not an operator fitted to complete values or appended
with a desired geometric factor.

Clear its fixed denominators, and remove the common \(q-1\) valuation
of its coefficients. Denote the first nonzero classical Laurent
symbol by \(P_0(M,L)\). A Laurent shift in \(T\), if originally
present, can first be removed by multiplying by a power of \(T\);
its classical contribution is a Laurent unit.

Choose the geometric lift for which the positive main meridian has
eigenvalues \(M,M^{-1}\). Define \(L_{\mathrm{geom}}\) to be the
preferred longitude eigenvalue on its \(M\) line, equivalently the
inverse eigenvalue on the source \(M^{-1}\) line. Let
\(A_{\mathrm{geom},\mathbb C}\) generate the height-one Laurent
prime of the actual oriented discrete-faithful eigenvalue germ
through \((M,L)=(1,-1)\).

Using the marked local reconstruction, peripheral rigidity and
negative-lift arguments described below, the conclusion is
\[
       A_{\mathrm{geom},\mathbb C}(M,L)
                     \ \mid\ P_0(M,L)
          \quad\text{in }\mathbb C[M^{\pm1},L^{\pm1}].
 \tag{4}
\]
The factor is defined up to a nonzero Laurent monomial. There is no
claim about its multiplicity or about other factors of \(P_0\).

## 2. The exact geometric identity before and after filling

The local nonparabolic character and native face-map constructions
give the same marked four-puncture representation. Their full boundary
tuples identify the original pure page gluing, and the actual ordered
Hurwitz collar gives the retained odd seam. The natural eigenflag
exchange is kept; the failed fixed-white odd chart is not used.

For the source wire \(E_e\) and circle coordinates \(Q_v\), the
actual auxiliary increments are
\[
 \rho_{v,e}=\frac{Q_v+E_e}{1+Q_vE_e},\qquad
 U_v=\sum_{e\ni v}\log\rho_{v,e}
                  -\epsilon_v\log Q_v,\qquad
 V_v=2\log Q_v .
 \tag{5}
\]
The edge equation is
\[
 (E_e+Q_v)(E_e+Q_v^{-1})
 (E_e+Q_w)(E_e+Q_w^{-1})
 =(E_e-1)^2(1-E_eM^2)(1-E_e/M^2).
 \tag{6}
\]
These are actual marked boundary words, not only trace coordinates.
Set
\[
                         f_e=\frac{M^2-E_e}{1-M^2E_e}.
 \tag{7}
\]

The peripheral rigidity proof has three independent parts.
First, differentiating (6) gives the exact source identity
\[
 d\log M\wedge d\log f_e
 +\frac12\sum_{v\in e}d\log\rho_{v,e}\wedge d\log Q_v=0.
 \tag{8}
\]
Second, the adjoint trace cup product and cochain Stokes identity on
the actual exterior give the same boundary form for its main
longitude and the pairs \((U_v/2,\log Q_v)\). The odd term in (5)
has zero wedge with \(d\log Q_v\). Thus the squared discrepancy
\[
 R=\frac{L_{\mathrm{aug}}^2}{\prod_e f_e^2}
 \tag{9}
\]
has zero derivative in every \(Q_v\).

Third, the generic source field is geometrically integral over
\(\mathbb C(M)\). Its independent edge squareclasses are
\[
 (Q_v-1)^2(Q_w-1)^2
              -4(M+M^{-1})^2Q_vQ_w .
 \tag{10}
\]
The elementary irreducibility and valuation proof is recorded in the
constants-field note. Hence (9) belongs to \(\mathbb C(M)\).
At every \(M_0\ne0\), the regular generic character matrices and
irreducible-pair intertwiners construct a local section of the actual
representation on which \(R\) and \(R^{-1}\) are units. This includes
the split source fibers at \(M_0=\pm i\), and the noncentral
parabolic values \(\pm1\). Consequently \(R=cM^k\).
Complete normalization gives \(c=1\), and the already marked
augmented cusp calculation fixes
\[
 L_{\mathrm{aug}}^2
       =M^{2a_{\mathrm{aug}}}\prod_e f_e^2,\qquad
 a_{\mathrm{aug}}=-w_\epsilon-\sum_v\epsilon_v .
 \tag{11}
\]
Here only the exponent is calibrated from the cusp derivative.
The full functional dependence follows from (8)--(10) and the
all-\(M_0\) unit argument.

Let \(\ell_v\in\{0,\pm2\}\) be the original crossing-circle linking
number with the main knot. The actual preferred filled longitude is
the augmented preferred longitude multiplied by
\(\mu_K^{\sum_vp_v\ell_v^2}\). Therefore
\[
 L_{\mathrm{fill}}^2=M^{2a(D)}\prod_e f_e^2,\qquad
 a(D)=a_{\mathrm{aug}}+\sum_vp_v\ell_v^2
                =-w(D)-\sum_vn_v .
 \tag{12}
\]
The last equality uses the original oriented crossing sign:
\(\ell_v^2=2(1+o_v)\) and
\(w(D)-w_\epsilon=-2\sum_vp_vo_v\).
No added geometric correction is inferred from the quantum phase.

## 3. The actual geometric branch at the filled complete point

The exponentiated filling equation from (5) is
\[
              \prod_{e\ni v}\rho_{v,e}=Q_v^{n_v}.
 \tag{13}
\]
It has many branches. The branch relevant here is fixed by the
original logarithmic first-charge equations, not by (13) alone.
Write \(Q_v=e^{i\tau_v}\), \(E_e=e^{2\pi ix_e}\). At \(M=1\),
the source first-charge equation is
\[
 \sum_{e\ni v}b_\tau(x_e,\tau_v)
             +\frac{in_v\tau_v}{2\pi}-i=0,
 \tag{14}
\]
where \(b\) is the original circle-incidence action.
Since \(\log\rho_{v,e}=-2\pi b_\tau\), equations (1), (5)
give exactly
\[
                     U_v+p_vV_v=-2\pi i .
 \tag{15}
\]
Replacing the final constant in (14) by \(-ic\), \(0\le c\le1\),
gives the original marked path from augmented completeness to the
smooth filled complete knot.

For the independent-long-power class, this is the branch identified
by the exact auxiliary Fourier/Legendre substitution and the marked
primitive filling proof. For the two quantitative all-circle
classes, the positive angular charts and their completion theorem
give that path directly. They retain the actual ordered page
decomposition and keep the main knot cusp unfilled.

The new nonparabolic chart agrees with those actual page matrices
at \(M=1\), with the same wire branch through \(E_e=i\), the same
ordered seams and the same half-twist calibration. Following the
marked angular path therefore identifies its point at \(c=1\)
with the actual oriented complete hyperbolic filled representation.
This is the representation-level anchor; equality of volumes or
cusp tangents would not replace it.

Now set \(M=e^{\pi it}\) and use the source's nondegenerate analytic
critical branch \(X_*(t)\) through that filled point. Its equations
are precisely (6), (13), with the logarithms of (14) retained.
They lie in the regular native/character charts after possibly
shrinking the \(t\)-disk.

At the filled point each auxiliary \(\operatorname{Im}\tau_v<0\).
Thus \(Q_v^2\ne1\), and its auxiliary longitude is semisimple
noncentral. The filling word commutes with that longitude and has
eigenvalue ratio one by (13); it is therefore projectively the
identity, not an undetected nontrivial parabolic. The constructed
representation factors through the actual filled knot group.
This remains true in a neighborhood of \(t=0\).

The main meridian coordinate \(M=e^{\pi it}\) is nonconstant.
The actual marked geometric germ is unramified over this meridian,
as established by the existing positive-gluing/representation
argument. Consequently the constructed germ is the geometric
deformation germ of that filled knot. A source critical point with
only the same complete value or tangent would not suffice; the
full group representation and filling relations above supply the
additional identification.

## 4. The sign required to pass from the square

Equation (12) leaves a two-valued ambiguity. It is fixed at the
actual complete filled knot, not by choosing the sign that agrees
with a desired source expression.

Take a once-bordered Seifert surface in the truncated knot complement.
A global oriented tangent frame on it, completed by its normal,
has trivial spin monodromy around its boundary because that boundary
is zero in \(H_1(S;\mathbb Z/2)\). The boundary-adapted tangent frame
winds by \(\chi(S)=1-2g\), an odd number. It therefore has
antiperiodic spin monodromy. Arrange the surface collar to meet the
cusp torus radially along the straight preferred longitude. Its
adapted frame is then a translation-invariant horospherical frame.
The lift of that frame path in \(\mathrm{SL}_2(\mathbb C)\)
ends at the positive unipotent translation, so antiperiodicity
means that the actual longitude holonomy is its negative.

Hence the preferred longitude has eigenvalue \(-1\) at the
complete filled knot. A spin structure can be obtained by restricting
one from \(S^3\); no special property of the source sum is involved.
Any two determinant-one knot holonomy lifts give the same longitude
sign, since the preferred longitude is zero in the knot's first
homology.

If a separate augmented lift is used, it has the same filled
longitude sign: the augmented homology class of that word is
\[
 [\lambda_{\mathrm{fill}}]
   =\sum_v\ell_v[\mu_v]
       +\sum_vp_v\ell_v^2[\mu_K]=0
               \quad\text{in }H_1(-;\mathbb Z/2).
 \tag{16}
\]
Thus a character changing the lift cannot change this word's sign.
A global rational SL lift of the entire source variety is unnecessary;
the actual filled geometric lift and a local germ suffice.

Every factor (7) is one at \(M=1\). Holomorphic continuation on the
connected filled germ now fixes (12) as
\[
 \boxed{\displaystyle
 L_{\mathrm{geom}}(M)
          =-M^{a(D)}\prod_e\frac{M^2-E_e(M)}{1-M^2E_e(M)}.}
 \tag{17}
\]
Without this negative-lift argument, the squared identity alone
would identify the geometric curve only up to \(L\mapsto-L\).

## 5. Retaining the reduced/full gauge in the operator argument

The published filtered-characteristic theorem has been read with its
actual normalization. Put
\[
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},\qquad
 d_N(M)=\eta_N\frac{M-M^{-1}}{M^N-M^{-N}},
 \qquad d_N(1)=\eta_N/N.
 \tag{18}
\]
On the microscopic chart \(M=q_N^s\), one has exactly
\[
 \frac{d_N(q_N^s)}{d_N(1)}=H_N(s)^{-1}.
 \tag{19}
\]
Thus \(F_N(q_N^s)/(K_NH_N(s))\) is the normalized full
modified-trace state. It is not obtained by deleting a peripheral
factor.

For \(f(M)=M-M^{-1}\), the exact shift ratio is
\[
 \frac{d_N(q_N^jM)}{d_N(M)}
                 =(-1)^j\frac{f(q_N^jM)}{f(M)}.
 \tag{20}
\]
The normalized full state therefore obeys
\[
 \widetilde P
   =\sum_{j=0}^{d}a_j(q,M)(-1)^j
                         \frac{f(M)}{f(q^jM)}T^j.
 \tag{21}
\]
Multiplication on the left by \(\prod_{j=1}^df(q^jM)\)
clears these additional denominators. Its first classical symbol is
\[
                       f(M)^dP_0(M,-L).
 \tag{22}
\]
The sign character and the meridian divisor are both retained.

The exact finite source supplies all orders on a finite union of
translated microscopic disks away from the ordinary resonances.
Its logarithm has the proved degree filtration
\[
 \log\frac{F_N(q_N^s)}{K_NH_N(s)}
       \sim\sum_{r\ge1}N^{-r}p_r(s),\qquad
                         \deg p_r\le r+1.
 \tag{23}
\]
Its top diagonal is the analytic critical value \(S(t)\) of the
original first-charge action plus
\(\sum_e[2J(x_e)-J(x_e+t)-J(x_e-t)]\) and the exact
scalar term \(\pi ia(D)t^2/2\).

With \(h=\log q\), \(u=\log M=hs\), define
\[
        \mathcal S(u)=\pi i\{S(u/(\pi i))-S(0)\}.
 \tag{24}
\]
The filtration regrades (23) as
\(h^{-1}\mathcal S(u)+\sum_{j\ge0}h^jA_j(u)\).
The \(j\)-step ratio has constant \(h\)-coefficient
\(e^{j\mathcal S'(u)}\). The translated-source expansions justify
inserting every shift in the fixed operator (21).
The substitution \(u=hs\) is injective on
\(\mathbb C[[h,u]]\), so its exact formal equation yields
\[
 f(e^u)^dP_0(e^u,-e^{\mathcal S'(u)})=0.
 \tag{25}
\]
The factor \(f(e^u)^d\) is nonzero in this integral domain.
Canceling it in (25) is justified; it was not discarded from the
operator or from the finite invariant.

The rational action derivative in the same theorem gives
\[
 -e^{\mathcal S'(u)}
    =-M^{a(D)}\prod_e\frac{M^2-E_e(M)}{1-M^2E_e(M)}.
 \tag{26}
\]
Equations (17), (25), (26) show
\[
                         P_0(M,L_{\mathrm{geom}}(M))=0.
 \tag{27}
\]
This is a full germ identity. No fixed-\(M\) WKB theorem or
asymptotic statement with \(s\) growing with \(N\) has been assumed.

## 6. The irreducible factor and its coefficient field

The Laurent prime of the analytic germ in (27) is nonzero, because
\(P_0\ne0\), and it contains no nonzero polynomial in \(M\)
alone, because \(M\) varies on an open disk. It therefore has
height one in \(\mathbb C[M^{\pm1},L^{\pm1}]\). This ring is a
unique factorization domain, so the prime is generated by one
irreducible Laurent polynomial. The representation identification
in Section 3 makes that generator precisely the selected geometric
eigenvalue factor. Equation (27) proves (4).

Suppose \(P\) has coefficients in \(\mathbb Q(q,M)\), and choose
the denominator clearing over \(\mathbb Q\). The prime obtained by
evaluating \(\mathbb Q[M^{\pm1},L^{\pm1}]\) on the same geometric
germ is again a nonzero height-one prime. Let
\(A_{\mathrm{geom},\mathbb Q}\) generate it. Then
\[
           A_{\mathrm{geom},\mathbb Q}\mid P_0
             \quad\text{over }\mathbb Q.
 \tag{28}
\]
Its complex factorization contains the selected geometric factor
and any conjugate components forced by the rational coefficient
field. This is the correct rational conclusion. One must not
silently assume that a particular complex geometric component is
defined over \(\mathbb Q\), or replace (28) by a claim that the
entire conventional A-polynomial divides \(P_0\).

## 7. Dependency audit and limitations

The operator step is exactly Sections 4--7 of the current
/private/tmp/murakamis_dream-publication/notes/actual_main_meridian_filtered_characteristic.md.
The all-level existence input is finite_sum_annihilator.md; it
constructs a genuine fixed operator from the actual finite cut
state independently of this factor argument.

The new geometric inputs are the native character comparison,
the full page/Hurwitz boundary gluing, the peripheral-ratio
rigidity note, and the all-main-values reconstruction. Their
constants-field step is proved in
/private/tmp/md-all-circle-source-geometric-integrality-and-constants.md.
The sign input is
/private/tmp/md-preferred-longitude-negative-lift-seifert-frame.md.
The actual filled anchor is the existing marked joint-filling
theorem or the quantitative all-circle completion theorem,
including its charge path and preferred-cusp continuation.

This corollary uses the new geometric adapter only for the covered
all-circle tree classes. The published filtered theorem also covers
more general strict trees with bare junctions; their analytic
source-selected characteristic alone does not supply this new
geometric identification. A knot admitting a covered all-circle
presentation of course has the same intrinsic geometric factor
regardless of how it is presented elsewhere.

No equality of minimal quantum operators, full classical
A-polynomials, or whole annihilator ideals has been proved. No
multiplicity statement, arbitrary short-twist extension, or
asymptotic formula through ordinary-color resonances is inferred.
