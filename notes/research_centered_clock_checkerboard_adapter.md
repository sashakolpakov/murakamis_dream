# The centered-clock checkerboard adapter on the original Morse source

Private written proof, 17 November 2026. The original centered physical
clock has a global determinant-ratio convention. The adapter retains
the dual carry, the original marked coefficient phase, and the signs
of both protected variables. It does not substitute geometric clocks
into the finite clock algebra or identify a selected geometric period.

## 1. Source, coloring, and centered labels

Use the connected original flat-plat source of [H], with its literal
two-strand boxes, cups, caps, and unrestricted marked cap. Put
\[
 N\ge3,\qquad d=N-1,\qquad q=e^{\pi i/N},\qquad Q=q^2.
 \tag{1}
\]
All coupons are the original full polynomials in the pair Casimir.
The repeated-node data and any external parameters stay in these
polynomials. This is a fixed-root statement.

There is a global checkerboard coloring \(\epsilon_f\in\{1,-1\}\)
of the original face variables, opposite across every physical
strand. One proof assigns the color by parity of crossings of a
path from the exterior. A closed path crosses the planar mod-two
cycle formed by the strands an even number of times. The parity is
therefore independent of the path. At a box all four strand ends
have even total incidence, and cups and caps simply continue a
strand. In the actual local face order \((x,b,c,y)\), the signs are
\[
 (\epsilon_x,\epsilon_b,\epsilon_c,\epsilon_y)
       =(\epsilon,-\epsilon,-\epsilon,\epsilon).
 \tag{2}
\]
In the trivalent expansion the matching edge separates the two middle
faces, which have the same sign; it is not an additional physical
strand across which the color should change. Repeated face labels
are retained. The two protected faces \(u,v\), outside and inside
the original marked cap, have opposite signs.

Define the constant change of formal face variables
\[
 L_f=\epsilon_f w_f.
 \tag{3}
\]
The exact original face-clock equations [H, (3)--(7a)] give
\[
 Q^i=-q^{-1}\frac{L_{\rm left}}{L_{\rm right}},
 \qquad
 X_i:=qQ^i=-\frac{L_{\rm left}}{L_{\rm right}}
                  =\frac{w_{\rm left}}{w_{\rm right}}.
 \tag{4}
\]
Here “left” and “right” mean the ordered neighboring regions of the
literal upward physical port. At a box this reads
\[
 X_a=\frac{w_x}{w_b},\quad X_{b_0}=\frac{w_b}{w_y},
 \qquad X_{a'}=\frac{w_x}{w_c},\quad
 X_{b_0'}=\frac{w_c}{w_y}.
 \tag{5}
\]
Thus the same checkerboard change works at every box. In particular
\[
 X_aX_{b_0}=X_{a'}X_{b_0'},\qquad
 Q^{a'-a}=\frac{X_{a'}}{X_a}=\frac{w_b}{w_c},\qquad
 C=\frac{X_{a'}}{X_{b_0}}
        =\frac{w_xw_y}{w_bw_c}.
 \tag{6}
\]
No independent \(q\)-dependent unit is chosen at each crossing.
The middle-face shift \(a'-a\) of [H] is distinct from the
crossing transfer \(a'-b_0\) whose exponential is \(C\) in [F].
Both are differences of physical heads, so neither has a half shift.

## 2. Actual duals and the logarithmic carry

The literal reversed physical head is \(i^\vee=d-i\). Exactly,
\[
 X_{i^\vee}=qQ^{d-i}=X_i^{-1},\qquad
 X_iX_{d-i}=1.
 \tag{7}
\]
These identities include both level parities. At a cup or cap the
ordered region pairs are \((o,z)\) and \((z,o)\), where \(o\) is
outside and \(z\) inside. Equations (4) therefore give precisely the
two inverse ratios in (7), with the actual first/second head order.
An auxiliary channel head is not assigned the physical half shift
in (4); its original integer degree equation remains as in [H].

On a chosen logarithmic lift put
\[
 \ell_i=\frac{2\pi i}{N}\left(i+\frac12\right).
 \tag{8}
\]
For logarithms \(\rho_f=\Log w_f\), the exact multiplicative identity
(4) is equivalently
\[
 \ell_i=\rho_{\rm left}-\rho_{\rm right}+2\pi i k_i,
 \qquad k_i\in\mathbb Z.
 \tag{9}
\]
These integers are the actual chosen source carries. Indeed if
\(\Log L_f=\rho_f-\pi i\chi_f\), with
\(\epsilon_f=(-1)^{\chi_f}\), then the extra half of
\(1-\chi_{\rm left}+\chi_{\rm right}\) is an integer because the
two colors differ. Thus the sign change introduces no fractional
logarithmic obstruction. For complementary physical heads one must
retain
\[
 \ell_i+\ell_{d-i}=2\pi i,\qquad k_i+k_{i^\vee}=1.
 \tag{10}
\]
The second identity uses the reversed region order at the dual port.
Replacing both inverse logarithms by negatives would lose this carry.
Continued complex heads use (9) on the recorded lift, rather than
independently resetting their logarithms.

On the actual finite grid, a further exact relation is
\[
 X_i^N=q^NQ^{Ni}=-1.
 \tag{11}
\]
Arbitrary geometric determinant ratios need not satisfy (11).
Consequently (4) is not a homomorphism from this finite clock algebra
to arbitrary geometric scalar clocks.

## 3. Compatibility with the complete determinant development

For this comparison, additionally supply the same ordered physical-port
diagram with the complete regular determinant development of [F].
The finite coefficient identity alone does not assign such a
development to arbitrary coupon choices. Retain one global auxiliary vector \(P\)
and the propagated region vectors \(s_f\), and set
\[
 w_f=\det(P,s_f).
 \tag{12}
\]
We use the open set on which the relevant determinants are nonzero.
Across an oriented arc the region transport is its actual meridian,
or its inverse when the arc is read backwards. The Wirtinger
identity is exactly the consistency relation at a crossing. These
are the region words of [F, Section 2], not new independently
chosen local vectors.

At a positive crossing, [F, (2.1)--(2.2)] gives
\[
 s_M=a s_0,\quad s_P=c s_0,\quad s_R=a c s_0,
 \qquad
 A=\frac{w_0}{w_M},\quad B=\frac{w_M}{w_R},\quad
 C=\frac{w_0w_R}{w_Mw_P}.
 \tag{13}
\]
These are exactly (5) and its transfer ratio, with the literal
input/output ordering of that crossing. Reading the negative
crossing backwards gives its actual inverse assignment. The
complete classical clocks \(A,B\) are thus realized by the centered
labels \(X\); the corresponding raw finite-head clocks are
\(q^{-1}A,q^{-1}B\). This distinction retains the half-index shift.

There is no additional frame switch at a Morse extremum. To check it
explicitly, use the outside and inside regions \(o,z\) of that turn.
If one oriented leg has \(s_z=\mu s_o\), the reverse leg has
\(s_o=\mu^{-1}s_z\). The auxiliary vector \(P\) and the two region
vectors remain the same. The ordered ratios are respectively
\(\det(P,s_o)/\det(P,s_z)\) and its inverse. This proves compatibility
with (7) at each actual cup and cap. It does not interchange the
global columns \(P,S\), replace the dual by an unrelated reference
frame, or identify the two generic peripheral eigenflags.
The same argument applies along each intervening strand, so the
comparison is global at the complete multiplicative-label level.

In particular, for any such geometric assignment one may define
complex physical labels by
\[
 i=\frac{N}{2\pi i}\Log X-\frac12
 \tag{14}
\]
with (9)--(10) retained. This agrees with the centered sampling
convention and its actual dual. It does not say that these complex
labels are physical integer states, satisfy (11), solve the
finite-\(N\) stationary equations, or give an off-critical
representation for independently varying all face variables.

## 4. Full coefficient, phases, and the protected sign

Let \(\mathcal P_N(L)=\prod_eH_{f_e}(L)\) be the entire homogeneous
numerator of [H], of degree \(dR\). The exact original marked source,
with its separately recorded external scalar lines unchanged, is
\[
 Z_N=[\prod_{f\ {\rm ordinary}}L_f^d]\,\mathcal P_N(L),
 \qquad n_u=n_v=0.
 \tag{15}
\]
The substitution (3) gives the exact polynomial identity
\[
 Z_N=
 \left(\prod_{f\ {\rm ordinary}}\epsilon_f^{-d}\right)
 [\prod_{f\ {\rm ordinary}}w_f^d]\,
           \mathcal P_N\bigl((\epsilon_f w_f)_f\bigr).
 \tag{16}
\]
Thus at odd \(N\) the displayed coefficient phase is one; at even
\(N\) it is the recorded product of the ordinary checkerboard signs.
Reversing every color leaves (16) unchanged by total homogeneity.
The original crossing scalars, cups, caps, mark, and all coupon
normals remain in (15)--(16). Fixed-root external parameter
derivatives commute with this constant change. No genuine-\(q\)
normal statement is obtained by differentiating these root formulas.

For an explicit mark check, [H] and [M] give its ratio to the
ordinary cap as
\[
 \frac1N(L_v/L_u)^d
       =\frac{(-1)^d}{N}(w_v/w_u)^d.
 \tag{17}
\]
The original second-head convention has not changed. Its sign is
part of the global phase accounting in (16).

For example, on the explicitly specified complete frame
\[
 S=(r,h)^t,\quad P=(1-r,-h)^t,\quad
 \mu=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\]
direct determinants give \(w_u=h\), \(w_v=h(1+h)\).
With any nonzero ordinary anchor \(W=w_a\), define dephased ratios
\(x=w_u/W,\ y=w_v/W\). Then
\[
 y/x=1+h,\qquad L_v/L_u=-(1+h),\qquad
 L_u/L_a=(\epsilon_u/\epsilon_a)x,\quad
 L_v/L_a=(\epsilon_v/\epsilon_a)y.
 \tag{18}
\]
Thus the determinant cover can still use \(y/x=1+h\), provided
the sign factors remain inside the full polynomial as in (16).
They cannot be silently omitted when that cover is compared to
the original protected coefficient.

## 5. Exact scope and complete direct sources

Equations (3)--(10) provide a global original-label adapter,
including all Morse duals. Equations (12)--(14) identify its
complete regular determinant assignment. Equation (16) transports
the entire original coefficient with its known phase. These facts
do not replace the independent ordinary coefficient variables by
their values on a two-dimensional framing orbit, commute a protected
residue with transverse stationary phase, or determine the original
cycle's geometric coefficient. Generic peripheral eigenflag
corrections in [F, Section 6] also remain outside this complete
comparison.

All three complete texts and their used implications were read.
No programs, numerical tests, or public/frozen edits are used.

| Label | Source | SHA-256 |
|---|---|---|
| H | [Homogeneous full Casimir face source](actual_homogeneous_casimir_face_source.md) | a7d89f310f2cb4193ab73ef49f715198b224d1c3756d84c4cb940d7fa850c2f2 |
| F | [Actual crossing fundamental cycle](crossing_fundamental_cycle.md) | 0d7d7da0f5cf4fe0d16907e7e999d5ce7980f7ff39d437df167c99ca30205b0f |
| M | [Original marked Morse coefficient](actual_original_marked_face_coefficient.md) | 746c903675953b25fd89475ed0e2635e4bae7e9498ceed10d66d58fc4d4790fa |
