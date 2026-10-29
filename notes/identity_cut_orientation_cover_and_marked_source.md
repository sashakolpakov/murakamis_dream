# The identity cut has an exact orientation-cover source

27 October 2026. This is a finite whole-source identity for the actual
four-port tensor. It replaces neither the state nor its selected cap.
It introduces an orientation factor together with its compensating
measure, keeps the cap's marked sheet, and retains every finite band.
The comparison with the geometric momentum below is a principal local
comparison; a whole Gaussian/source comparison is not inferred.

## 1. Retain the original cap and every port band

Use the literal tensor and port order of
[the physical two-cut construction](actual_two_cut_framing_port_reconstruction.md).
With zero extension outside all four physical ranges, put

\[
 \mathcal F_T(x,y;\xi,\eta)
 =\sum_{a,b,\mu,\nu}T_{a+\mu,b+\nu;a,b}
                       x^a y^b\xi^\mu\eta^\nu.
\]

The first original balanced cut has matrix coefficients 1/N; the
second cut closes by its original identity, without a new pivotal
weight. Thus, with all original pivots and external scalar lines
already inside T,

\[
 F(\eta)=\mathcal F_T(1,1;1,\eta),\qquad
 \Phi_{\rm id}(T)=\frac1N[\eta^0]F
       =\mathop{\rm Res}_{\eta=0}F(\eta)\frac{d\eta}{N\eta}.       \tag{1}
\]

The sums over the first output and input remain in F. This is not
the normalized trace of a reshaped two-position matrix. In particular,
charged current tensors use all their first-port bands as in (1).
The same formula works coefficientwise for every whole crossing or
source coupling; no specialization of those coefficients is required.

## 2. An exact orientation factor with the compensating measure

Introduce the quadratic cover

\[
 u=\eta+\eta^{-1},\qquad v=\eta-\eta^{-1},\qquad v^2=u^2-4.
\]

Its involution is eta to eta inverse, fixing u and changing v to -v.
On this cover the following is a literal equality of rational forms:

\[
 \boxed{\quad
 F(\eta)\frac{d\eta}{N\eta}
       =[vF(\eta)]\frac{du}{N(u^2-4)}.\quad}                  \tag{2}
\]

Indeed du=v d eta/eta. Consequently the original source equals the
marked residue of the orientation-twisted section G=vF against the
new measure. The multiplication by v is the nearest-band difference
on the full kernel. Its compensating measure is essential.

There is a precise parity qualification. G is odd if F is even under
eta inversion. For arbitrary actual T the correct law is instead

\[
                    G\circ\iota=-v(F\circ\iota).              \tag{3}
\]

Thus (2) is an orientation twist without an assumed involution symmetry
of the whole braid word. It does not declare the scalar function G
odd when the actual tensor does not have that symmetry.

Multiplication M_v identifies the full Laurent kernel space with its
submodule v times that space. On this image every actual linear current
A transports as M_v A M_v inverse, and its co-source transports by (2).
The inverse is used only on that image. This is a strict source-preserving
change of presentation, not division by a possibly vanishing selected
period. All endpoint/corner summands are part of the same full kernel.

## 3. The original cap marks the sheet at infinity

The point eta=0 determines a particular preimage of u=infinity:

\[
 v/u\longrightarrow-1,\qquad
 \eta=(u+v)/2,\qquad
 t=1/u=\frac{\eta}{1+\eta^2}=\eta+O(\eta^3).                  \tag{4}
\]

The last equality gives an actual local uniformizer of order one.
Residues in eta and t therefore agree, including their signs. On this
sheet v is asymptotic to -u. For a constant F, the right side of (2)
is asymptotic to -F du/(Nu), whose standard residue at u=infinity
is +F/N. The other preimage, eta=infinity and v/u tending to +1,
has residue -F/N. Taking an unmarked sum of the two sheet residues
would cancel this constant cap. The original tensor fixes the first
sheet in (4); there is no additional choice of an odd cycle.

The apparent poles of du/(u^2-4) at u=2,-2 introduce no new poles
in the TOTAL form: at eta=1,-1 the factor G=vF cancels them. This
uses the actual finite Laurent nature of F. The measure may not be
evaluated independently and then assigned its own endpoint terms.

## 4. A finite tail formula, not just the nearest coefficient

Write F=sum F_j eta^j and G=sum G_j eta^j. Near the marked eta=0,

\[
 \frac{du}{Nv^2}=\frac{d\eta}{N(\eta^2-1)}
                  =-\frac1N\sum_{k\geq0}\eta^{2k}d\eta.
\]

Consequently the exact new source is

\[
 \Psi(G)=-\frac1N\sum_{k\geq0}G_{-2k-1}.                     \tag{5}
\]

Only finitely many coefficients contribute for any actual tensor.
Since G_j=F_(j-1)-F_(j+1), the partial sum through k=K is

\[
             -\frac1N\sum_{k=0}^K G_{-2k-1}
                    =\frac{F_0-F_{-2K-2}}N.                 \tag{6}
\]

The final coefficient outside the full support vanishes, proving
Psi(vF)=F_0/N exactly. Formula (6) is the retained finite endpoint
term. Dropping it early, using only -G_-1/N, or replacing (5) by
the constant coefficient of vF changes the source.

For the literal two-cut unknot tensor, which is the flip tensor,

\[
 F_{\rm unknot}(\eta)
    =\sum_{j=-(N-1)}^{N-1}(N-|j|)\eta^j.                     \tag{7}
\]

The original cap and (5) both give one. The constant coefficient of
vF is zero. Keeping only -G_-1/N gives 2/N for N at least two;
the remaining finite tail contributes (N-2)/N. This actual tensor
already detects the distinction between an odd insertion at the old
source and the source-preserving orientation change (2).

## 5. Whole clocks and their connection term

Let r be an invertible whole clock parameter. The change eta to r eta
acts on the cover by

\[
 \begin{split}
 u_r&=\tfrac12(r+r^{-1})u+\tfrac12(r-r^{-1})v,\\
 v_r&=\tfrac12(r-r^{-1})u+\tfrac12(r+r^{-1})v.
 \end{split}                                                   \tag{8}
\]

It preserves u squared minus v squared and the marked eta=0 point.
It also preserves the original logarithmic measure exactly:

\[
       \frac{du_r}{v_r}=\frac{du}{v},\qquad
       \iota\,\tau_r\,\iota=\tau_{r^{-1}},                  \tag{8a}
\]

where tau_r is eta to r eta and iota is eta to eta inverse.
For the actual whole Q dilation set r=Q in (8). These transports
form the multiplicative torus with its inversion involution;
the resulting group is dihedral in this precise sense, not
automatically nilpotent. At a primitive finite root the dilation
itself has finite order. None of these identities drops its
whole normal dependence before specialization.
For G=vF the actual transformed section representing F(r eta) is

\[
                \widetilde S_rG=\frac{v}{v_r}G(u_r,v_r).       \tag{9}
\]

In particular a clock does not act by an unaccompanied u substitution.
Writing D=eta partial_eta=v partial_u+u partial_v, differentiation
of (9) gives the exact connection

\[
 \widetilde D=D-u/v,\qquad M_v D=\widetilde D M_v,
 \qquad
 (\widetilde DG)\frac{du}{Nv^2}=\frac1N d(G/v).                \tag{10}
\]

Its marked residue is zero. All finite clock derivatives follow
before taking any quantum normal or large-N limit. Although (9)-(10)
have denominators, the corresponding sections lie in the transported
image and the total original form is retained.

Physical port clocks have mixed kernel actions. In the full kernel,
input clocks Q^a,Q^b act by x to Qx,y to Qy; output clocks Q^(a+mu),
Q^(b+nu) act by (x,xi) to (Qx,Qxi) and (y,eta) to (Qy,Qeta).
Thus (8)-(10) transport precisely the eta component while keeping the
simultaneous y rescaling for an output clock. General boundary
braiding/prefix adapters still act in their original order. Independent
whole crossing couplings commute with M_v, and differentiating them
preserves (2), (5) and every finite endpoint in (6).

## 6. Compatibility with the actual prefix framing cover

The independent proof of
[the actual prefix chart](prefix_adapted_two_position_framing_cover.md)
retains U=mu_j...mu_1, V=mu_(j-1)...mu_1, k=ell_U/ell_V and

\[
 z=s(k-1),\qquad
 D=(-1)^jz(p-p^{-1}),\qquad
 \Omega_{cut}=\frac{\ell_V}{BD}d\log A\wedge d\log B.          \tag{11}
\]

Here p is the actual balanced local wave momentum and B=1/k at
completeness. The two nearest actual output exchange bands have
principal ratios p inverse and p, respectively. Distinguish the finite
Fourier-band variable eta_F in Sections 1--5 from the geometric
parameter eta_geo=p inverse. The boundary action gives the principal
Fourier incidence eta_F p=1. This is not a coordinate isomorphism of
the original source spaces or a map of their cycles. On this incidence
the geometric orientation factor is

\[
 v_{geo}=p^{-1}-p,\qquad D=(-1)^{j+1}zv_{geo}.                \tag{12}
\]

The orientation factor of the exact cap cover consequently has the
correct geometric sign line. Retaining the actual inverse-prefix
clock, whose whole expression is (q/M)^(j-1) product_(i<j) Q^(J_i),
gives the principal equality

\[
 \ell_V^{-1}(R_{(+1,-1),0}-R_{(-1,+1),0})\Omega_{cut}
       =\frac{(-1)^{j+1}}{Bz}d\log A\wedge d\log B.           \tag{13}
\]

The density alone is not generally odd: ell_V can differ on the two
sheets. Formula (13) includes precisely the prefix factor that would
be lost by substituting a developed meridian for the physical one.

Equations (2) and (13) are compatible orientation formulas on that
incidence; they are not an equality of their whole selected period
complexes. In particular eta_F and the physical position B are
independent before that correspondence. Closing the second port by
the eta_F constant term does not sum its input position b or identify
that sum with a physical B cycle.
The marked residue in (4)-(6) involves all finite bands and their
endpoint, whereas the existing transverse Gaussian theorem handles
fixed bounded port offsets on a regular interior chart. Transporting
that full residue/endpoint through the Gaussian comparison remains
necessary. In particular (13) alone is not permission to insert a new
odd observable into the original knot period.

There is also a direct comparison with the UNINSERTED principal cap
measure, including its rational base Jacobian. Write sigma=(-1)^j,
t_W=Tr W and

\[
 A_0=c_U+s t_U,\qquad A_1=c_V+s t_V.
\]

In the reference frame Tr(JC)=c_C+t_C. In the moving cut frame it is
s(beta-gamma)+(1-s)t_C. Using (4.1) of the prefix note gives

\[
 u_{geo}=p+p^{-1}=\frac{\sigma(A_0-kA_1)}{s(k-1)},\qquad
 \left.\frac{\partial u}{\partial k}\right|_s
            =\frac{\sigma(A_1-A_0)}{s(k-1)^2}.                 \tag{14}
\]

The extra s derivative vanishes after wedging with d log A. Together
with D=-sigma s(k-1)v and the density in (11), this proves

\[
 \boxed{\quad
 \frac{\Omega_{cut}}{\ell_V}
   =\frac{k-1}{A_1-A_0}\,d\log A\wedge\frac{du_{geo}}{v_{geo}}
   =\frac{k-1}{A_1-A_0}\,d\log A\wedge\frac{d\eta_{geo}}{\eta_{geo}}.
 \quad}                                                       \tag{15}
\]

This equality is on the further regular chart A_1-A_0 nonzero and
k not one. It includes the actual inverse-prefix clock ell_V inverse
and an explicit rational Jacobian on the two-position base. Applying
(2) to the final one-form in (15) gives the same orientation-twisted
section and compensating measure as an algebraic formula. To use it
for the period still requires an actual transform of the source and
its physical input-position sum. No such transform follows from (15).
For a genuine quadratic prefix this Jacobian chart is generically
nonempty; a linear prefix or exceptional first-position fiber requires
another coordinate rather than division by its vanishing Jacobian.

Formula (15) identifies the geometric density's algebraic one-form
shape with the logarithmic measure appearing in the finite cap.
It does not identify their source functionals, transport the marked
eta_F=0 cap, sum the independent physical input-position b, or carry
the finite tail (6) through the transverse Gaussian. Those remain
the precise global comparison data.

### 6.1. The geometric compactification has a zero-residue boundary

There is an exact algebraic boundary test on the geometric incidence
cover, not an image of the original marked finite cap or its cycle.
In this subsection eta means eta_geo and u,v are its cover coordinates.
Solving (14) for k gives

\[
 k=\frac{su+\sigma A_0}{su+\sigma A_1},\qquad
 k-1=\frac{\sigma(A_0-A_1)}{su+\sigma A_1}.                   \tag{16}
\]

At the geometric eta_geo=0 boundary, u is asymptotic to eta inverse
and v to minus eta inverse. Consequently

\[
 k-1=\frac{\sigma(A_0-A_1)}s\eta+O(\eta^2),\qquad
 D\longrightarrow A_0-A_1.                                  \tag{17}
\]

At the other preimage eta=infinity the limit is D=A_1-A_0.
The two points of this GEOMETRIC compactification reach k=1, or
physical B=1, on two algebraic sheets. This does not say that the
original eta_F cap maps to either point. At k=1 one has det(U-V)=0,
so the exact discriminant is (A_0-A_1)^2. If c_U-c_V is nonzero,
the root formula r=(c_C+s h_C-D)/(2c_C) shows that r, and hence
ell_V, is finite at (17). On this regular boundary chart,

\[
 \frac{\ell_V(k-1)}{A_1-A_0}
       =-\frac{\sigma\ell_V(0)}s\eta+O(\eta^2).              \tag{18}
\]

Thus the full leading framing density Omega_cut itself is regular
at that geometric boundary and has ZERO eta_geo logarithmic residue.
The apparent eta logarithm in (15) is canceled by its rational
Jacobian. A nonzero cap source cannot be obtained by discarding
that Jacobian and declaring a regular constant amplitude there, even
if a proposed source map assigned the cap to that boundary. This is
a property of the principal prefix chart, not an assertion that such
a source map exists or that the selected quantum period vanishes.

For example the genuine figure-eight prefix in Section 6 of the
prefix note, at s=1 and u_shape squared plus u_shape plus one equal
to zero, has

\[
 c_U-c_V=1,\quad A_0-A_1=3+u_{shape},\quad
 r\longrightarrow-2,\quad \ell_V\longrightarrow2+3u_{shape}.
\]

All displayed regularity conditions hold there. For a scalar
meromorphic amplitude a(eta), the exact residual to compute is

\[
 [\eta^0]\left(a(\eta)
                   \frac{\ell_V(k-1)}{A_1-A_0}\right)d\log A. \tag{19}
\]

A holomorphic amplitude gives zero. If its only negative term is
a_-1/eta, the result is -sigma ell_V(0) a_-1/s times d log A;
larger poles require the corresponding full finite coefficient
sum in (19). The actual finite kernel has negative Fourier-band
powers whose order grows with N. They cannot be substituted into
a(eta_geo) without the actual source transform. That transform must
retain the original source, norm, physical input-position sum,
endpoints and any escaping/polar block contribution. The bounded
interior Gaussian theorem does not evaluate (19) as the original cap.

[The actual boundary-moment and Ward-atom calculation](actual_negative_band_boundary_moment_and_ward_atom.md)
makes this distinction testable. The finite weighted negative-band
functional is exactly an original source paired with a K-Ward current
and does not equal the identity source on actual signed tensors.
An original negative factorial circuit does supply an explicit
inverse-norm pole, but its presence in the selected full geometric
source is a separate transport question.

## 7. Reproducible actual tensor checks

[The independent audit script](../experiments/audit_identity_cut_orientation_cover.py)
uses literal signed braid tensors with their original pivotal,
half-Cartan, framing and peripheral scalar lines. It checks (1),
(5)-(6), the unknot formula, whole input/output clock rescalings and
the connection (10). It also tests the same finite source formula
on every port matrix unit with endpoint indices included.
The results are recorded in
[the audit output](../experiments/identity_cut_orientation_cover_results.json).
These checks validate the finite source change; they are not a
global geometric period or volume asymptotic calculation.
