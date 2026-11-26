# An explicit quarter-disk bound for the moving shortened-edge current

Private finite-source theorem, 9 November 2026. The fixed complete-height
current and its vertical connection give an explicit neighborhood on
which the entire original moving right current is exponentially smaller
than the selected action. The resulting packet concerns the source with
full first edge and shortened second edge. It is not a statement about
the full canonical two-edge polynomial on this neighborhood.

No mathematical numerical evaluation, saved-value arithmetic or
frozen-source edit is used.

## 1. Source and statement

Retain the unchanged definitions of the
[single-current assembly](research_mixed_next_inner_three_single_remaining_current.md):
\[
\begin{gathered}
D=N-1,\quad U=\lfloor N/2\rfloor-1,\quad
q=e^{\pi i/N},\quad\eta_N=(-1)^D,\quad C_{N,3}=q^{3D^2/4},\\
K_N^{\mathrm{ord}}(X,Y)=\sum_{j=0}^{D}e_j(X)e_j(Y),\qquad
K_N^{<,\mathrm{ord}}(X,Y)=\sum_{j=0}^{U}e_j(X)e_j(Y),\\
K_N^<(t,u)=K_N^{<,\mathrm{ord}}(-2\cos t,-2\cos u),\qquad
W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2},\\
Q_N^{\mathrm{sh}}(u)=\phi_N^{(X)}
 \left[R_N(X)^3K_N^{\mathrm{ord}}(-2,X)
                  K_N^{<,\mathrm{ord}}(X,-2\cos u)\right].
\end{gathered}                                                     \tag{1}
\]
The superscript on \(Q_N^{\mathrm{sh}}\) specifies its second edge;
its first edge and its Hermite trace are full. Define
\[
\begin{gathered}
t_*(u)=a_*(u)-iH(u),\qquad S(u)=S_3(0,u),\qquad s(u)=\Re S(u),\\
t_3=t_*(0)=a_3-iH_0,\qquad M_3=s(0),\qquad
r=2^{-16},\\
\mathcal Q_r=\{u:\Re u\ge0,\ \Im u\le0,\ |u|\le r\}.
\end{gathered}                                                     \tag{2}
\]
These critical data have their original branches and constants.

For fixed \(u\), let \(\mathcal R_N(u)\) be the original moving
current, with the original prefactor,
\[
\mathcal R_N(u)=-\frac{N^2C_{N,3}}{\pi i}
 \int_{\pi/2-iH(u)}^{5\pi/6-i/10}
 \sin t\,K_N^<(t,0)K_N^<(t,u)e^{3iNt^2/(4\pi)}W_N(t)\,dt,
                                                                    \tag{3}
\]
where any path in the open lower half-plane may be used.

**Theorem.** At both parities, uniformly for \(u\in\mathcal Q_r\),
and all sufficiently large levels,
\[
\boxed{\qquad
                  |\mathcal R_N(u)|\le C e^{N\{s(u)-r\}}.
\qquad}                                                          \tag{4}
\]
Consequently the full-first/short-second source in (1) has
\[
Q_N^{\mathrm{sh}}(u)=C_{N,3}N^{-3/2}\mathcal A(u)e^{NS(u)}
                                        (1+O(N^{-1})),
                              \qquad u\in\mathcal Q_r,
                                                                    \tag{5}
\]
uniformly through both parities. The amplitude \(\mathcal A\) is
the original nonzero coefficient of the single-current assembly.
Neither (4) nor (5) asserts a full-disk bound, an outgoing derivative
estimate, or the same packet for the full canonical polynomial
\(P_{3,N}(0,u)\).

## 2. A written lower bound for the complete-height reserve

The [fixed-height current theorem](research_mixed_next_inner_three_fixed_height_right_current.md)
uses
\[
\Delta_0=\frac{(\pi/2-a_3)^2}{8\pi},\qquad
\varepsilon_0=\frac{\Delta_0}{2}.
                                                                    \tag{6}
\]
We prove the explicit inequalities
\[
                       \varepsilon_0>\frac1{8192}=8r,
                       \qquad \Delta_0>16r.
                                                                    \tag{7}
\]

At the complete output write
\(v=2\cos(t_3/2)=x+ib\). The original cubic continuation gives
\[
\frac32<x<\frac{15}{8},\qquad \frac13<b<\frac23,\qquad
1=\frac x2(x^2-3b^2+4b-3),\qquad 0<H_0<1.
\]
The displayed real cubic identity rearranges exactly to
\[
x^2-b^2=1+\frac2x+2(b-1)^2
                 >1+\frac{16}{15}+\frac29=\frac{103}{45}.
                                                                    \tag{8}
\]
Since \(v^2=2+2\cos t_3\), this implies
\(\cos a_3\cosh H_0>13/90\). The positive series gives
\[
\cosh1\le1+\frac12+\frac{1/24}{1-1/30}<\frac85.
\]
Therefore
\[
\cos a_3>\frac{13}{144},\qquad
\pi/2-a_3>\sin(\pi/2-a_3)=\cos a_3>\frac{13}{144}.
                                                                    \tag{9}
\]
Using \(\pi<4\), (6),(9) give the exact comparison
\[
\varepsilon_0>
 \frac{169}{144^2\,16\pi}
 >\frac{169}{162\cdot8192}>\frac1{8192}.
                                                                    \tag{10}
\]
This proves (7) without evaluating the critical point.

## 3. Quantitative movement of the original phase data

On the phase disk \(|u|\le1/4\), put
\[
v(u)=2\cos(t_*(u)/2),\qquad c(u)=v(u)/2,
\qquad\Delta(u)=3v(u)^2-4iv(u)-3.
\]
This disk lies in the original cubic continuation rectangle.
The strict guards in that theorem give
\[
\Re v>3/2,\quad1/3<\Im v<2/3,\quad |c|<1,\quad
\Re\Delta>19/4,
\quad v'=-\frac{\sin(u/2)}{\Delta}.
                                                                    \tag{11}
\]
For the lower bound on \(\Re\Delta\), write \(v=x+ib\)
and use
\(\Re\Delta=3x^2-3(b-2/3)^2-5/3>19/4\).
Also
\[
|\sqrt{1-c^2}|^2=|1-c^2|
 \ge|\Im(c^2)|=2\Re c\Im c>\frac14.
                                                                    \tag{12}
\]
The root in (12) is the original \(\sin(t_*/2)\), and the
modulus bound is independent of its sign. Differentiating the
original inverse cosine and using (11) gives
\[
t_*'(u)=\frac{\sin(u/2)}{\Delta\sqrt{1-c^2}}.
                                                                    \tag{13}
\]
The absolute sine series yields, for \(|u|\le1/4\),
\[
|\sin(u/2)|\le\sinh(|u|/2)
 \le\frac{|u|/2}{1-1/384}<|u|\quad(u\ne0).
\]
Equations (11)--(13) therefore imply \(|t_*'(u)|<|u|\)
for nonzero \(u\) in this disk. Radial integration proves
\[
|t_*(u)-t_3|\le\frac{|u|^2}{2},\qquad
                   |H(u)-H_0|\le\frac{|u|^2}{2}.
                                                                    \tag{14}
\]

We also need a phase bound, without assuming a finite packet on
this disk:
\[
                         |S''(u)|<1\qquad(|u|\le1/4).
                                                                    \tag{15}
\]
Here is a direct check on the same branch. The cubic gives
\(c'=-\sin(u/2)/(2\Delta)\), hence \(|c'|<1/4\).
The elementary bounds
\[
|\sin(u/2)|\le\frac{48}{383}<\frac17,\qquad
|\cos(u/2)|\ge\cos(1/8)\ge\frac{127}{128}
\]
give \(|\tan(u/2)|<1/6\) and \(|\sec^2(u/2)|<4/3\).
For \(w=c(u)\tan(u/2)\), it follows that
\[
|w|<1/6,\qquad |w'|<1/24+2/3<3/4,\qquad
                              |\sqrt{1+w^2}|>5/6.
\]
The original derivative
\(S'=-\pi^{-1}\operatorname{arsinh}w\) now proves
\(|S''|<9/(10\pi)<1\). Evenness gives \(S'(0)=0\), so
another radial integration yields
\[
                     s(u)\ge M_3-\frac{|u|^2}{2}.
                                                                    \tag{16}
\]
All statements (11)--(16) concern the calibrated phase. They
do not extend a finite-source theorem by themselves.

## 4. The fixed current and the exact vertical connector

Let \(\mathcal R_N^0(X)\) be the fixed-height current on
\[
\pi/2-iH_0\longrightarrow5\pi/6-iH_0
                                \longrightarrow5\pi/6-i/10,
\]
with its original definition and normalization. Equations (9),(24)
of the fixed-height theorem give
\[
\begin{split}
|\mathcal R_N^0(-2\cos u)|
   &\le C e^{N(M_3-\varepsilon_0/4)},
                                      &&|\Im u|\le\varepsilon_0,\\
\mathcal R_N(u)
   &=\mathcal R_N^0(-2\cos u)+\mathcal V_N^0(u),
\end{split}                                                       \tag{17}
\]
where the retained connector is
\[
\mathcal V_N^0(u)=-\frac{N^2C_{N,3}}{\pi i}
 \int_{\pi/2-iH(u)}^{\pi/2-iH_0}
 \sin t\,K_N^<(t,0)K_N^<(t,u)
                  e^{3iNt^2/(4\pi)}W_N(t)\,dt.
                                                                    \tag{18}
\]
Its sign is unchanged. In the depth variable \(t=\pi/2-ih\)
the prefactor is \(+N^2C_{N,3}/\pi\), and the limits are
\(H(u)\) to \(H_0\).

For \(u\in\mathcal Q_r\), (7),(16),(17) imply
\[
|\mathcal R_N^0(-2\cos u)|
  \le C e^{N(M_3-2r)}\le C e^{N(s(u)-r)}.
                                                                    \tag{19}
\]
Indeed \(r<\varepsilon_0\) and \(r^2/2<r\).

We estimate (18) using the complete-period slit theorem, not
an own-phase packet for its second factor. By (14), its depth
lies between \(H_0\) and \(H(u)\), with distance at most
\(r^2/2\) from \(H_0\). The original guards and \(r\le1/4\)
place this segment in the fixed compact
\[
                       t=\pi/2-ih,\qquad1/4\le h\le1.
                                                                    \tag{20}
\]
On this compact the
[slit theorem, Theorem 2 and Corollary 3](research_mixed_next_first_short_edge_slit_plane_bound.md)
gives, for each fixed \(\tau>0\),
\[
\begin{split}
|K_N^<(t,0)|&\le C_\tau e^{N(\Re\psi(t,0)+\tau)},\\
|K_N^<(t,u)|&\le C_\tau N
 e^{N(\Re\psi(t,0)+\tau)+U|\Im u|}.
\end{split}                                                       \tag{21}
\]
The second bound retains its exact outside degree \(U\). It
follows from the full real outside-period bound and ordinary
Chebyshev continuation, so it applies to the literal shortened
kernel at every complex \(u\) under consideration. It is not
inferred from an estimate at a proper subset of physical nodes.

For the complete phase
\(\Phi(t,0)=2\psi(t,0)+3it^2/(4\pi)-it\), the original return
has imaginary part strictly between \(-\pi/2\) and zero on (20).
At \(a=\pi/2\), its exact height derivative is therefore
\[
-\frac14<
\partial_h\Re\Phi(\pi/2-ih,0)
  =-\frac2\pi\Im\operatorname{arsinh}\tan((\pi/2-ih)/2)
                                      -\frac14
<\frac34.
                                                                    \tag{22}
\]
The complete-height phase comparison in the fixed-current theorem
starts at \(\Re\Phi(\pi/2-iH_0,0)\le M_3-\Delta_0\).
Consequently every point of (18) has
\[
\Re\Phi(t,0)\le M_3-\Delta_0+\frac{3r^2}{8}.
                                                                    \tag{23}
\]
The full multiplier satisfies
\[
|W_N(\pi/2-ih)|
       \le\frac{e^{-Nh}}{(1-e^{-N/4})^2}\le C e^{-Nh}.
                                                                    \tag{24}
\]
All its Fourier charges are included. Its leading decay is already
the charge term in (23).

Choose the explicit tolerance \(\tau=r\) in both bounds (21).
Equations (21)--(24), \(U<N/2\), and \(|\Im u|\le r\)
give
\[
|\mathcal V_N^0(u)|
 \le C N^3
  \exp N\left\{M_3-\Delta_0+\frac{3r^2}{8}+\frac r2+2r\right\}.
                                                                    \tag{25}
\]
The sine and connector length are bounded; the latter is at most
\(r^2/2\). Since \(\Delta_0>16r\) and \(3r^2/8<r/2\),
the rate in braces is less than \(M_3-13r\). Absorbing \(N^3\)
in a further \(r\), and then using (16), proves
\[
|\mathcal V_N^0(u)|\le C e^{N(M_3-12r)}
                               \le C e^{N(s(u)-11r)}.
                                                                    \tag{26}
\]
Combining (17),(19),(26) proves (4), with the entire connector
retained and bounded rather than omitted.

## 5. The shortened-source consequence and its exact scope

The original single-current assembly, uniformly on its closed
positive lower rectangle, states
\[
Q_N^{\mathrm{sh}}(u)
 =C_{N,3}N^{-3/2}\mathcal A(u)e^{NS(u)}(1+O(N^{-1}))
                 +\mathcal R_N(u)+O(e^{N(s(u)-\epsilon)}),
                                                                    \tag{27}
\]
for some fixed \(\epsilon>0\). The amplitude is the original
nonzero one and is bounded away from zero there. This assembly
includes its separate first-edge trace-level replacement error,
all original currents and normal data, and the odd simple node.

The set \(\mathcal Q_r\) lies in that source domain. Substitution
of (4) into (27) makes both additional terms exponentially small
relative to the nonzero main term, uniformly on this set. This
proves (5) with the original scalar and amplitude. The unquantified
constant \(\epsilon\) in the other already paid groups remains
positive; no value for it is inferred here.

The full canonical two-edge source \(P_{3,N}(0,u)\) agrees with
\(Q_N^{\mathrm{sh}}(u)\) at every double physical outgoing node,
by literal Newton zeros. Their off-grid polynomials have different
degree ranges. No identity or sufficiently small off-grid difference
between them has been proved here. In particular \(r=2^{-16}\)
is not asserted to be an eligible full-\(P_{3,N}\) disk radius in
the whole-frequency constant audit. The proven source set is the
closed positive lower quarter-disk, and the result alone gives
neither a full complex disk nor outside derivatives or a complete
outer-transfer estimate.

## Frozen source bindings

| Source | SHA-256 |
|---|---|
| Fixed-height all-node current | 6f5a45805c83881ff84573a523072e35f2213d9323f2a6d245711b03128c6c7f |
| Original cubic continuation | 8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a |
| Slit-plane full-row and shortened-kernel bounds | efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b |
| Single-current full finite-source assembly | 2c5be7138aed7dabbb06f04010c602ee095fa8ceb62ec213e75e4d628aa95421 |
