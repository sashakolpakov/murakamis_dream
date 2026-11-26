# Joining a finite collection of marked filled blocks at one circle

Research note, 2 November 2026. This extends the geometric argument
for repeated zero blocks to a fixed finite library of actual,
already proved partially filled blocks. The blocks may have different
complex boundary curvatures. Their common circle still has one
primitive longitude, one carrier, and its original integer filling
power.

The uniform small-saddle estimate is the analytic input. This note
identifies that saddle with the marked geometric filling and fixes
its absolute volume. It also explains why terminal blocks can leave
no auxiliary circle to be filled later.

## 1. The fixed library

For each block type \(j\) retain a distinguished free reference
circle with angle \(t\), any other free angles \(\mathbf u\),
and a holomorphic phase \(W_j(t,\mathbf u)\). A block is included
only when the following facts have already been proved for its
actual original source and topology:

1. Its selected internal slopes are already filled, and it has a
   positive marked cell decomposition at zero free boundary angles,
   continuing on a small complex neighborhood.
2. Its incoming and outgoing reference interfaces have the original
   ordered ratio tables
   \[
   (-Q^{-1},-Q,-Q^{-1}),\quad(-Q,-Q^{-1},-Q),\qquad Q=e^{it}.
   \tag{1}
   \]
   These specify the complete triangle maps.
3. Its pure distinguished periods are
   \(U=-2\pi(W_j)_t\), \(V=2it\), with analogous formulas at
   its other free boundaries. Every internally filled primitive
   period remains at its prescribed \(2\pi\) value.
4. The main cusps remain complete, \(W_j\) is separately even
   in the free variables, and its absolute complete-boundary
   volume is \(2\pi\Re W_j(0,\mathbf0)\).
5. Its distinguished curvature is
   \[
              (W_j)_{tt}(0,\mathbf0)=-a_j+ib_j,\qquad a_j>0.
   \tag{2}
   \]

These are established for the zero-subtree blocks in
[their Conway geometric identification](research_zero_subtree_conway_geometry.md)
and for every fixed terminal crossing power \(|k|\ge2\) in
[the terminal-filling theorem](research_verified_terminal_fillings_and_long_remainder.md).
Other proved blocks can be included when they have these same
marked interfaces and source properties; the definition does not
grant them to an arbitrary partial filling.

For a terminal power \(k\), the calibrated phase is
\[
 W_k(u)=\operatorname{stat}_s
       \left[\psi(s,u)+\frac{ik}{4\pi}s^2-is\right].
 \tag{3}
\]
Its boundary curvature is
\[
                 W_k''(0)=-\frac{\cos(s_k/2)}{2\pi},
                 \qquad \Re\cos(s_k/2)>0.
 \tag{4}
\]
For \(k=\pm2\), the source phase in its elementary one-index
formula differs from (3) by \(\pm i\pi/2\). The exact factor
\(e^{\pm i\pi N/2}\) stays in the unit scalar. It is not a
change of the geometric action. The other terminal scalars
are likewise those specified in the terminal theorem.

Because the library is finite, there is one radius \(\rho>0\)
on which all its marked charts remain positive and
\[
        \Re(W_j)_{tt}(t,\mathbf0)<-a_j/2
                                      \quad (|t|\le\rho).
 \tag{5}
\]
In particular, for real \(t\) in this interval,
\(\Re(W_j)_t(t,\mathbf0)\) is strictly decreasing and
vanishes at zero.

## 2. Actual annular gluing

Choose \(m\) library entries, with repetitions allowed, and identify
their distinguished sectors at one original circle \(v\). This
circle has exactly these \(m\) incidences. All other outside
circles remain distinct unless their original marked assembly
explicitly identifies them.

The common value of \(Q\) in (1) matches the full labelled
two-triangle interfaces. Cut each reference torus along its
original disk longitude and glue the annuli in the prescribed
cyclic order. The meridian crosses the sectors once each; the
longitude remains one common primitive curve. This is the same
annular operation proved in Section 5 of the zero-subtree
geometry note and used in the terminal assembly.

Writing
\[
                    P_0(t,\mathbf U)=\sum_{j=1}^m
                                           W_j(t,\mathbf u_j),
 \tag{6}
\]
the actual central periods, after inserting its original carrier
\(\eta\) once, are
\[
          U_v=-2\pi(P_0)_t-i\eta t,\qquad V_v=2it.
 \tag{7}
\]
For the original integer coefficient \(p\), put \(n=\eta-2p\).
Then
\[
        U_v+pV_v=-2\pi\left((P_0)_t+\frac{in}{2\pi}t\right).
 \tag{8}
\]

At zero free boundary angles, the actual complete reference
interfaces glue isometrically, retaining their original cusp
markings. The free peripheral periods are zero; the main
meridians remain nonidentity parabolics and their commuting
peripheral elements are translations. The positive cusp
triangles have the original compact torus links. Thus the
remaining cusps are complete. The initial parent volume is
\[
                         2\pi\sum_j\Re W_j(0,\mathbf0).
 \tag{9}
\]
The blocks' already filled cores are smooth geodesic cores
of this parent. They are not filled again in this gluing.

## 3. Complex curvature and the original central power

Let
\[
               A=\sum_j a_j,\qquad B=\sum_j b_j,\qquad
               n_{\rm eff}=n+2\pi B.
 \tag{10}
\]
The effective parameter \(n_{\rm eff}\) is a real number
used only in the analytic saddle estimate. It is not a
new crossing power, carrier, or surgery coefficient.
The exact primitive equation remains
\[
             \sum_j(W_j)_t(t,\mathbf0)+\frac{in}{2\pi}t=ic,
                                  \qquad 0\le c\le1.
 \tag{11}
\]

Suppose the companion source argument constructs its branch
through zero with
\[
       |t(c)|\le\frac{7c}
                    {\sqrt{(2\pi A)^2+n_{\rm eff}^{\,2}}}.
 \tag{12}
\]
A sufficient extra geometric threshold is
\[
                     \frac7{2\pi m a_{\min}}<\rho,
                     \qquad a_{\min}=\min_j a_j>0.
 \tag{13}
\]
This threshold depends only on the fixed library. It is
uniform over all choices and orders of its \(m\) entries
and over every fixed signed original power \(n\).

**Theorem 1.** Under (12)--(13), the branch (11) is the
original positive central cone filling. Its other free
cusps remain complete and every previously filled
primitive slope stays fixed. At \(c=1\) the central
filling is smooth.

**Proof.** Each block stays in its fixed positive chart
by (12)--(13), and (1) glues their entire boundary maps.
Equation (8) gives the full period
\(U_v+pV_v=-2\pi ic\).
The derivative at zero is
\[
 t'(0)=\frac{i}{-A+i\,n_{\rm eff}/(2\pi)},\qquad
       \Im t'(0)=
       -\frac{A}{A^2+(n_{\rm eff}/(2\pi))^2}<0.
 \tag{14}
\]
If the branch later reached real \(t\) at positive charge,
the real part of (11) would give
\(\sum_j\Re(W_j)_t(t,\mathbf0)=0\).
By (5) this forces \(t=0\), contradicting \(c>0\).
Hence the original central core length
\(-2\Im t(c)\) is positive.

Each internal filled slope is already held fixed in its
block's holomorphic boundary response. Its positive core
length persists in the chosen chart. At other free
boundaries separate evenness makes the corresponding
period derivatives zero when their angles are zero.
Their longitudes and carrier corrections are also zero.
The full main-cusp and face-map identities remain those
of the original block geometries. Thus all the stated
completeness, winding, and primitive-curve assertions
hold on this cone path. \(\square\)

## 4. Absolute volume after the last central filling

The selected action is
\[
 S(c)=\sum_j W_j(t(c),\mathbf0)
                  +\frac{in}{4\pi}t(c)^2-ic\,t(c).
 \tag{15}
\]
Stationarity gives \(d\Re S/dc=\Im t(c)\).
All older core angles are fixed at \(2\pi\), so their
terms in Schläfli's differential are zero even when their
lengths vary. The central term is
\(-\tfrac12(-2\Im t)\,d(2\pi c)\).
Together with (9), this proves
\[
                       \operatorname{Vol}_{c=1}=2\pi\Re S(1).
 \tag{16}
\]
Known imaginary source constants, including those at
terminal powers \(\pm2\), remain exact unit factors and
do not alter (16).

If some free circles remain, (5) also makes the central
implicit derivative nonsingular, so the same marked
positive response continues for small outside boundary
angles. This is the geometric input for a subsequent
long-filling assembly, when the source theorem supplies
the required full boundary estimates.

## 5. The terminal-only star

Fix a finite set \(\mathscr K\subset\{k\in\mathbb Z:|k|\ge2\}\)
of original terminal crossing powers. Use its terminal
blocks (3) as the library. An original star with \(m\)
leaves has one distinguished boundary per terminal block
and no further free boundary after its center is filled.

Therefore, for sufficiently large \(m\) depending only on
\(\mathscr K\), the geometry above applies to every
assignment \(k_j\in\mathscr K\) at the leaves and every
fixed signed power \(n\) at the center, with the original
parity, marking, and component conditions retained.
After the central filling only the main cusps remain.
If the prescribed strand tracing gives a knot, (16) is
the volume of its complement.

This geometric conclusion requires no later long powers.
Combining it with the companion full-source theorem,
once that theorem has been proved for this finite library,
gives the original Kashaev volume identity for these
stars. This note proves the geometry and normalization;
the coherent trace estimate and its nonzero coefficient
remain the analytic part of that implication.

## 6. A common marked chart for every terminal power of magnitude at least two

The terminal library need not be finite. Its geometric constants can
be chosen uniformly over all integers \(k\) with \(|k|\ge2\). This
statement concerns the marked geometry and phase; uniform estimates
for the original finite sums are a separate analytic assertion.

The edge derivative on its branch through completeness is
\[
 \psi_t(t,u)=-\frac1\pi\operatorname{arsinh}
                    \bigl(\tan(t/2)\cos(u/2)\bigr).
 \tag{17}
\]
Write \(s=1/k\) and \(t=s\zeta\). The terminal equation becomes
\[
                  \zeta=2\pi+2\pi i\psi_t(s\zeta,u).
 \tag{18}
\]
At \(s=0\) its derivative with respect to \(\zeta\) is one.
The holomorphic implicit function theorem therefore gives one
solution \(\zeta(s,u)\) on a product neighborhood of \((0,0)\).
It is even in \(u\) and satisfies
\[
 \zeta(s,u)=2\pi-2\pi i\cos(u/2)s+O(s^2),\qquad
 t_k(u)=2\pi s-2\pi i\cos(u/2)s^2+O(s^3).
 \tag{19}
\]
The remainders are uniform on a smaller closed \(u\)-disk.
Here is an explicit bound. On \(|t|,|u|\le1/4\),
differentiating (17) gives
\[
 |\psi_{tt}(t,u)|
 \le
 \frac{\cosh(1/8)}
 {2\pi\cos(1/8)\sqrt{1-\sinh^4(1/8)}}<\frac15.
\]
Thus (18) is a contraction of \(|\zeta|\le7\) for complex
\(|s|\le1/64\), uniformly for \(|u|\le1/4\).
Cauchy's estimate for its \(\zeta\)-Taylor coefficients
therefore gives, for \(|s|\le1/128\),
\[
 \left|t_k(u)-2\pi s+2\pi i\cos(u/2)s^2\right|
          \le 14\cdot64^2\,|s|^3 .
 \tag{19a}
\]
This deliberately coarse bound is independent of \(k\)
and \(u\) in the stated disk.
For every sufficiently large positive or negative integer \(k\),
this is the selected terminal branch: at \(u=0\) it has the
correct sign of the real part and lies in the positive terminal
chart, whose selected solution is unique.

There is also an exact sign check for its core length. The
holomorphic quotient
\[
             Q_e(t,u)=\frac{\psi_t(t,u)}{t}
\]
extends across \(t=0\), where
\(Q_e(0,u)=-\cos(u/2)/(2\pi)\). Shrink the common edge chart so
that \(\Re Q_e<-c_0<0\). Rearranging the actual equation, rather
than just its first two Taylor terms, gives
\[
 t_k(u)=\frac{2\pi/k}{1-2\pi iQ_e(t_k(u),u)/k},\qquad
 \Im t_k(u)=
 \frac{4\pi^2\Re Q_e(t_k(u),u)}
      {k^2|1-2\pi iQ_e(t_k(u),u)/k|^2}<0 .
 \tag{20}
\]
Thus the previously filled core has positive length throughout
one common complex boundary disk for both signs of \(k\).
The core lengths tend to zero like \(k^{-2}\); no fixed positive
lower bound on their lengths has been assumed.

All original edge flags, tetrahedron shapes and face maps are
holomorphic at \((t,u)=(0,0)\). Choose a small fixed bidisk on
which its eight shapes remain positive. One can check positivity
directly with the criterion in
[the positive-edge theorem](research_positive_edge_global_monotonicity.md):
if \(a=\tan(t/2)\), \(b=\tan(u/2)\), then
\[
                    (\Im a)^2+(\Im b)^2<1
 \tag{21}
\]
is sufficient. For example the entire closed bidisk
\(|t|,|u|\le1/4\) satisfies (21), since
\(|\tan z|\le\tan|z|\) for \(|z|<\pi/2\) and
\(2\tan^2(1/8)<1\).
The full face chart is nonsingular on this positive domain.
Taking \(|s|\) and then the boundary radius small enough puts
all the solutions (18) in this same marked chart.

The finitely many remaining powers \(2\le|k|<k_0\) already
have positive marked terminal charts. Taking the minimum
of their boundary radii and the radius above gives one
\(\rho>0\) valid for every \(|k|\ge2\). The exact interface
tables (1), primitive periods and internally fixed filling
equations hold on this common disk. Their identities have
not been replaced by their limiting \(k=\infty\) values.

The filled tube is determined by those original primitive
curves. Its meridian period is still \(-2\pi i\), its
longitudinal period is \(2it_k(u)\), and (20) keeps the
latter loxodromic with positive core length. Continue the
original marked cell and tube construction from \(u=0\)
along a radial segment in this common disk. No cell
flattens, no defining face triple collides, and the
peripheral axis does not become parabolic. The meridian
winding stays one, so the completion remains a smooth
filled tube throughout. The common object here is a
boundary-parameter disk; there is no claim of a uniform
positive core length or a uniform metric lower bound on
the tube radius.

The phases themselves have a joint holomorphic extension
at \(s=0\):
\[
 \mathcal W(s,u)=
 \psi(s\zeta(s,u),u)
       +\frac{is}{4\pi}\zeta(s,u)^2-is\zeta(s,u),
 \qquad \mathcal W(0,u)=\psi(0,u).
 \tag{22}
\]
At \(s=1/k\), this is exactly the calibrated phase \(W_k\)
of (3). In particular
\[
       W_k''(0)\longrightarrow-\frac1{2\pi}
                      \quad (|k|\longrightarrow\infty).
 \tag{23}
\]
Together with (4) for the finitely many smaller powers,
this gives
\[
 \inf_{|k|\ge2}a_k>0,\qquad
 \sup_{|k|\ge2}|b_k|<\infty,\qquad
 W_k''(0)=-a_k+ib_k.
 \tag{24}
\]
The compact parameter set \(|s|\le s_0\), followed by the
finitely many exceptional charts, gives uniform bounds
for the higher boundary derivatives as well. After a
final common shrinkage,
\[
                \Re W_k''(u)<-\tfrac12a_k
                  \qquad (|u|\le\rho,\ |k|\ge2).
 \tag{25}
\]

Consequently the geometric threshold (13) can be made
independent of the magnitudes and signs of all terminal
powers. If the companion source theorem supplies its
uniform small-saddle estimate and coherent asymptotic for
this whole terminal family, the conclusion of Section 5
holds for arbitrary assignments \(|k_j|\ge2\), with one
leaf-count threshold and any fixed signed central power.
The phase factors at \(k_j=\pm2\) remain as in Section 1.
This strengthening does not remove the analytic hypothesis.
