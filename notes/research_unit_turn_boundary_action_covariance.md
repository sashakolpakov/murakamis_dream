# The lifted unit-turn shear and its boundary-work covariance

Private written proof, 16 November 2026.

The original iterated unit turn has an exact quadratic primitive in
the polarization where \(J=TCT\) is diagonal. Its state map and its
operator pullback have opposite shear signs. The primitive fixes the
change in the lifted period row and outside work, while preserving
the boundary Legendre energy. Returning through the two original
turns retains two unit-charge Fourier-sector terms. These facts do
not identify the resulting correspondence with a positive change
of the original parent's angle assignment.

## 1. Exact source and the marked diagonal primitive

Retain
\[
 N\ge2,\quad D=N-1,\quad q=e^{\pi i/N},\quad
 \eta=(-1)^D,\quad \kappa=q^{D^2/2},\quad
 P_N(Z)=2T_N(Z/2)+2,
\]
\[
 \mathcal A_N=\mathbb C[Z]/(P_N),\qquad
 \phi_N(e_i e_j)=\mathbf1_{i+j=D},\qquad
 K_N(Z,W)=\sum_{j=0}^D e_j(Z)e_j(W).
 \tag{1}
\]
The physical turn satisfies \(Te_j=e_{D-j}\), hence
\[
 (TF)(Z)=\phi_W[K_N(Z,W)F(W)],\qquad T^2=1.
 \tag{2}
\]
All products in a traced variable are in the full algebra, including
the first normals at double roots. Ordinary free variables and any
joint spectator remain unreduced.

For a fixed integer \(n\), use the original operators
\[
 V_n=\kappa^nTR^{-n}T,\qquad C F=ZF,\qquad
 J=TCT,\qquad D_n=V_nCV_{-n}.
 \tag{3}
\]
The positive physical angular lifts for a diagonal copy are
\[
 Z=-2\cos t,\qquad t_j=\pi-(2j+1)\pi/N,\quad
 0\le j<\lfloor N/2\rfloor.
 \tag{4}
\]
The crossing's full physical jets are represented by
\[
 R^n:\quad C_{N,n}e^{inNt^2/(4\pi)},\qquad
 C_{N,n}=e^{\pi i nD^2/(4N)}.
 \tag{5}
\]
At odd \(N\) the remaining simple root has lift \(t=0\).
Formula (5) specifies the original lift, not a periodic extension
of its Gaussian to arbitrary angular preimages.

**Proposition 1.** In the \(J\)-diagonal polarization, the exact
full-jet multiplier of \(V_n\) is
\[
 TV_nT=\kappa^nR^{-n}:
 \qquad C_{N,n}e^{-inNt^2/(4\pi)}
       =d_{N,n}e^{Ng_n(t)},
 \tag{6}
\]
where
\[
 g_n(t)=\frac{in}{4\pi}(\pi^2-t^2),\qquad
 d_{N,n}=e^{-i\pi n/2+i\pi n/(4N)}.
 \tag{7}
\]
Thus the leading additive constant is \(in\pi/4\); it has not
been chosen by calibration at a stationary point.

*Proof.* The exact identity \(TV_nT=\kappa^nR^{-n}\) follows from
\(T^2=1\). Since \(\kappa^n=C_{N,n}^2\),
\(\kappa^nC_{N,-n}=C_{N,n}\). Expanding \(D^2/N=N-2+1/N\)
gives (6)--(7). Equality of the Gaussian representatives and their
first spectral derivatives proves the full-jet statement, also at
\(N=2\); the odd simple value uses (5) at zero. \(\square\)

For a fixed logarithmic lift,
\[
 g_n(t+2\pi k)-g_n(t)=-ink\,t-i\pi nk^2,\qquad k\in\mathbb Z.
 \tag{8}
\]
Consequently exponentiating the spectral coordinate alone does not
retain this primitive. In particular its linear lift term cannot be
discarded in a period-row comparison.

## 2. State shear, inverse operator pullback, and the cubic

On a local angular chart let \(S\) be a holomorphic phase and
\[
 p=S'(t),\qquad \xi=e^{-2\pi p},\qquad \lambda=p\,dt.
 \tag{9}
\]
The sign is fixed by (4): increasing the physical row by one shifts
\(t\) to \(t-2\pi/N\), whose leading multiplier on \(e^{NS(t)}\)
is \(e^{-2\pi S'(t)}\).

**Theorem 2.** The lifted state correspondence of (6) is
\[
 \chi_n:(t,p)\longmapsto
            \left(t,p-\frac{int}{2\pi}\right),\qquad
 \chi_n^*\lambda-\lambda=dg_n.
 \tag{10}
\]
It preserves \(d\lambda\). In contrast, the principal symbol of the
conjugated operator \(D_n\) is the symbol of \(C\) pulled back by
\(\chi_n^{-1}\).

More explicitly, write \(y=-2\cos t\),
\[
 a=\frac{2-y}{2+y}=\cot^2(t/2),\qquad b=2+2a,
\]
on a chart avoiding \(y=\pm2\). In this polarization the symbols
of \(C\) and \(D_n\) are
\[
 x=b-a(\xi+\xi^{-1}),\qquad
 x_n=b-a(e^{-int}\xi+e^{int}\xi^{-1}).
 \tag{11}
\]
They satisfy exactly the original classical twist recurrence
\[
 x_{n+2}=8-yx_{n+1}-x_n.
 \tag{12}
\]
Thus the transformed boundary condition is \(x_n=2\), rather than
the unchanged equation \(x=2\).

*Proof.* Multiplication by (6) sends \(S\) to \(S+g_n\), with the
scalar \(d_{N,n}\) retained separately. Differentiation gives (10).
It also gives \(\xi_{\rm out}=e^{int}\xi_{\rm in}\).
An operator annihilating the input therefore pulls back using
\(\xi_{\rm in}=e^{-int}\xi_{\rm out}\), proving the inverse sign.

For a check directly from the original operators, the physical
difference formula for \(J\), in the \(C\)-diagonal basis, is
\[
 (Jf)(c(j))=c_0f(c(j))
    -A_j[f(c(j+1))-f(c(j))]
    -B_j[f(c(j-1))-f(c(j))],
 \tag{13}
\]
where \(c(j)=2\cos((2j+1)\pi/N)\), \(c_0=q+q^{-1}\), and
\[
 A_j=\frac{s_{j+1}^4}{s_{2j+1}s_{2j+2}},\qquad
 B_j=\frac{s_j^4}{s_{2j}s_{2j+1}},\qquad
 s_h=2\sin(h\pi/N).
 \tag{14}
\]
Both coefficients tend to \(a=\cot^2(t/2)\) in the chart (4).
After conjugating by \(T\), \(C\) is represented by this \(J\),
while \(D_n\) is represented by \(R^{-n}JR^n\).
The forward crossing ratio is exactly
\[
 \frac{R^n(t-2\pi/N)}{R^n(t)}
        =e^{-int+in\pi/N}
 \tag{15}
\]
on the specified Gaussian lifts; the backward ratio has limiting
multiplier \(e^{int}\). This proves (11) independently of the
phase notation (9). Since \(e^{it}+e^{-it}=-y\) and
\((2+y)b=8\), (12) follows. The finite operator recurrence and
its cubic are already exact in the pinned operator source.
No source amplitude is inferred by taking these symbols. \(\square\)

## 3. Lifted rows and the invariant boundary energy

Write \(t=s+ih\) and set
\[
 P=-\pi S'(t)=K+iG,\qquad dS=-P\,dt/\pi.
 \tag{16}
\]
The letters \(K,G\) are the real and imaginary parts of this
boundary momentum. They are not assumed to arise from positive
square cells. For a fixed real normalization constant \(E_*\), put
\[
 E_b=E_*-\pi\Re S+hG.
 \tag{17}
\]
When \(S\) is an original unfilled edge or component primitive,
this is its boundary Legendre expression, with its original
constant retained.

**Theorem 3.** For real \(n\), the shear (10) has the exact laws
\[
 S_n=S+g_n,\qquad P_n=P+\frac{int}{2},\qquad
 K_n=K-\frac{nh}{2},\qquad G_n=G+\frac{ns}{2},
 \tag{18}
\]
\[
 \Re S_n-\Re S=\frac{nsh}{2\pi},\qquad
 E_{b,n}=E_b,\qquad
 K_n\,ds+h\,dG_n=K\,ds+h\,dG.
 \tag{19}
\]
In particular, for the row \(c=-G/\pi\),
\[
 c_n=c-\frac{ns}{2\pi}.
 \tag{20}
\]
At the lower height \(h=-H\), the real action change is
\(-nHs/(2\pi)\), exactly the change in the work
\(-HG/\pi\).

*Proof.* Differentiate (7), multiply by \(-\pi\), and take real
and imaginary parts. Its constant is purely imaginary for real
\(n\). Thus \(\Delta\Re S=nsh/(2\pi)\) and
\(h\Delta G=nsh/2\), which cancel in (17).
Also (16)--(17) give \(dE_b=K\,ds+h\,dG\); substitution of
(18) proves its invariance directly. Equation (20) is then
immediate. \(\square\)

If a separately recorded power \(m\) is used to define
\(\rho=G-ms/2\), then
\[
 G_n-(m+n)s/2=G-ms/2.
 \tag{21}
\]
This is an algebraic rule for keeping a reference row invariant.
It does not identify \(m+n\) with the power of an unchanged parent
vertex. The diagonal multiplication in (6) is \(R^{-n}\):
it shifts an action's crossing exponent by \(-n\), as (18) states.
The two uses of a power in this bookkeeping must not be interchanged.

There is a precise convexity consequence when an independent real
energy \(E(s,G)\) is supplied on a domain \(\mathcal D\). Set
\[
 L_n(s,G)=(s,G+ns/2),\qquad
 \widetilde E=E\circ L_n^{-1}\quad\hbox{on }L_n\mathcal D.
 \tag{21a}
\]
An existing positive definite Hessian remains positive definite:
\[
 \nabla^2\widetilde E
 =(L_n^{-1})^{\mathsf T}(\nabla^2E)L_n^{-1}.
 \tag{21b}
\]
If \(dE=K\,ds+h\,dG\), its transformed differential has the
coefficients in (18). The same statement applies to any finite
set of independent boundary pairs. This preserves the supplied
energy on its transformed domain. It does not identify
\(L_n\mathcal D\) with the unchanged square-angle body or with
the literal angle domain of a post-pruning graph.

## 4. Returning through the original turns

Use \(Z_v=-2\cos v\) for an ordinary output boundary. Equations
(1)--(3) give the all-level exact source identity
\[
 (V_nF)(Z_v)=
 \kappa^n\phi_{Z_t}\phi_{Z_u}
 \left[
 K_N(Z_t,Z_v)R^{-n}(Z_t)K_N(Z_u,Z_t)F(Z_u)
 \right].
 \tag{22}
\]
It holds coefficientwise with arbitrary other variables and
joint spectators. No first normal, odd simple value, or crossing
carrier is removed. Multiple insertions of (22) may be composed
in their actual order in any fixed marked network.

Here is the lifted action of a specified local Fourier sector of
(22). Suppose the chosen original edge primitives \(\psi\) and
an input boundary primitive \(S(u)\) are holomorphic on the
declared chart, with
\[
 \psi_u(u,t)=-r_{u,ut}/\pi,\quad
 \psi_t(u,t)=-r_{t,ut}/\pi,
 \qquad \psi(0,0)=M_\infty.
 \tag{23}
\]
The selected unit-charge sector of the two lower trace kernels
has action
\[
 \mathscr A_n(u,t;v)=
 S(u)+\psi(u,t)+\psi(t,v)-i(u+t)
                  -\frac{int^2}{4\pi}+\frac{in\pi}{4}.
 \tag{24}
\]
The terms \(-iu\) and \(-it\) are the first Fourier aliases of
the two unit traces, not optional choices of row lift. The
remaining finite carrier is \(d_{N,n}\) from (7).

Indeed on a lower angular line the exact grid kernel is
\[
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}
        =\sum_{\ell\ge1}\ell\eta^{\ell-1}e^{-iN\ell t}.
 \tag{25}
\]
The sector \(\ell_u=\ell_t=1\) gives (24). Other horizontal
sectors replace the two displayed integers by their actual
\(\ell_u,\ell_t\); the original trace also retains its vertical
currents. Thus (24) is not asserted to be the phase of the
whole source (22).

On the critical relation of (24) the rows and boundary momentum
are exactly
\[
 S'(u)=\frac{r_{u,ut}}{\pi}+i,\qquad
 r_{t,ut}+r_{t,tv}+\frac{int}{2}=-\pi i,\qquad
 \partial_v\mathscr A_n=-r_{v,tv}/\pi.
 \tag{26}
\]
These follow by differentiating (24). The middle row is the
original unit row with filling power \(-n\), at the newly
introduced intermediate variable \(t\). If a local critical
value is formed, its exterior differential is the last
expression, together with the untouched spectator differentials.
Internal differentials vanish by (26). No existence, positivity,
nondegeneracy, or contribution of such a critical point is
assumed in this identity.

## 5. What is still needed for the parent comparison

The fixed-parent calibration uses its original coordinates
\[
 \rho_v=\sum_{e\ni v}g_{v,e}-n_vs_v/2,\qquad
 \Re\Phi_1=M_G-D_0/\pi
 \tag{27}
\]
on the original positive slice at the parent's heights.
Equations (18)--(21) give the local row and work transformation
in the \(J\) polarization. Equations (22)--(26) specify the
exact turns and lifted sector needed to return to the ordinary
boundary variables. Neither the cubic equation nor preservation
of (17) identifies these new variables with the parent's original
square incidences and powers.

In particular, at an original saturated endpoint set \(C\),
the ambient inequalities force the opposite incidences to zero.
The pinned parent theorem gives, with all surviving edges retained,
\[
 \mathcal E=\mathcal E_{\rm del}+r_C\pi M_\infty,\qquad
 M_G-A_C(0;z)=
 \frac{D_0(z)}{\pi}
       +\sum_{v\in C}H_v^0(c_v(z)-1).
 \tag{28}
\]
The \(r_C M_\infty\) constants already cancel from the surviving
action. They are not a second allowance available to pay for a
turned source bound. Formula (19) exhibits the same issue locally:
the twist changes the row and work, while leaving the boundary
Legendre expression fixed.

To apply (27) after arbitrary pruning one still needs a marked
identification of the correspondence (26) with the parent's
incidence data, including all reference-power changes and
logarithmic lifts, and a comparison on an admitted positive or
closed angle assignment. Such an identification must pull back
the complete differential and constants, not merely the
exponentiated cubic. An actual quantum estimate must additionally
retain the other sectors and currents in (25) and (22).
No such positivity-preserving identification or current bound is
proved here.

## 6. Coverage and direct sources

The exact conjugation, crossing carrier, trace kernel, and
fixed-parent calibration are prior results. The added content
is their signed lifted shear, the invariant boundary Legendre
expression, and the two-turn unit-sector row/work bookkeeping.
The general classical crossing relation and matched-disk
composition notes were searched for coverage; they concern
different boundary coordinate presentations and are not proof
dependencies here.

The following complete sources were read at the stated versions;
the used implications and all hashes were checked:

* [Original operator and branching identities](research_unit_turn_finite_band_branching_operator.md),
  SHA256 31d9f574c7dc3aaac07e4eb50c131b3328be46b3c2a2ef46f9dae7f0c4ddb9cb.
  The full prior readback is retained at this unchanged pin;
  the kernel, conjugation, physical difference action and
  all-integer recurrence were rechecked.
* [Original full-period current](research_full_period_current_charge_convolution.md),
  SHA256 3f74b9824ecbf0b71a79b17959c7208f650103f95932192cfba87c7a7aa05595.
  The complete source was freshly reread, including the
  full-jet crossing lift and the complete trace rectangle.
* [Fixed-parent global calibration](research_fixed_parent_height_global_calibration.md),
  SHA256 268da098a6650065dc2abada9ce7c1bd8029abc33feb59783a67f03cd25a7bf0.
  The complete source was freshly reread, including the
  original phase, rows, saturated-edge constants and outside work.

Only written mathematics, source reads and hashes were used.
No mathematical program, numerical experiment, test or build
was run. Frozen notes and public manuscripts are unchanged.
