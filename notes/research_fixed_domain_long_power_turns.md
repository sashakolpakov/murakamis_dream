# Iterating long crossing powers on one fixed boundary disk

The one-step [large-power turn theorem](research_uniform_large_power_turn.md)
allows its output disk to be smaller than the input disk. That loss is
avoidable for the original complete edge kernel. The reason is a
centered complex-boundary estimate: the rate at an outer real trace
angle can be compared directly with the bare edge action at the same
complex outside boundary, rather than with its value at completeness.

This note proves that estimate, including the first normal needed by
the trace, and then closes the one-boundary estimates under arbitrarily
many long-power turns. One power threshold works at every step. The
length of the word is fixed before the level tends to infinity; no
simultaneous limit in word length or powers is asserted.

## 1. Two estimates for the full original edge

Write \(D=N-1\) and
\[
 K_N(t,u)=\sum_{k=0}^{D}e_k(-2\cos t)e_k(-2\cos u).
 \tag{1}
\]
The sum in (1) is never replaced by a low-index sum in the statements
below. The established edge theorem gives a holomorphic expansion
\[
 K_N(t,u)=N^{-3/2}a_e(t,u)e^{N\psi(t,u)}(1+O(N^{-1}))
 \tag{2}
\]
on a fixed bidisk, with a nonzero amplitude and
\(-\psi''(0,0)=(2\pi)^{-1}I\). The established global estimate is
\[
 |K_N(t,v)|\le CN^d
 e^{N\{M_\infty-c_e(1-\cos t)-c_e(1-\cos v)\}},
 \qquad t,v\in[-\pi,\pi],\quad c_e>0.
 \tag{3}
\]
The passage from retained indices to (2)--(3), including high indices
and both parities, is given in Section 5 of
[the uniform terminal-family note](research_uniform_terminal_family_and_star_fillings.md).

**Lemma 1 (centered complex boundary).** There are fixed positive
constants \(r_e,\gamma_e\) such that
\[
 |K_N(t,u)|\le CN^d
 e^{N\{\Re\psi(0,u)-\gamma_e(1-\cos t)\}}
 \quad(t\in[-\pi,\pi],\ |u|\le r_e).
 \tag{4}
\]
For every fixed \(0<r<\pi\), the same estimate, with the loss
\(\gamma_e(1-\cos(r/2))\), holds at polynomial cost for the first
derivative in \(z=-2\cos t\), uniformly on \(r\le|t|\le\pi\).

*Proof.* Choose a fixed \(0<a<1/4\) and a positive \(a_e^*\)
such that (2) holds on a neighborhood of \(|t|,|u|\le2a\) and
\[
                         \Re[-\psi''(t,u)]\ge a_e^*I
 \tag{5}
\]
there. For real \(|t|\le a\), evenness and integration twice give
\[
 \Re\psi(t,u)\le\Re\psi(0,u)-a_e^*t^2/2
             \le\Re\psi(0,u)-a_e^*(1-\cos t).
 \tag{6}
\]
The bounded amplitude in (2) proves (4) in this region.

For fixed real \(t\), the function of \(u\) in (1) is an even
trigonometric polynomial of degree at most \(D\). Dropping the
second angular loss in (3) and applying the polynomial maximum
principle inside and outside the unit circle gives
\[
 |K_N(t,u)|\le CN^d
 e^{N\{M_\infty-c_e(1-\cos t)+|\Im u|\}}.
 \tag{7}
\]
Evenness and holomorphy give
\(|\psi(0,u)-M_\infty|\le L_e|u|^2\) on a fixed small disk.
Choose \(0<r_e<a\) so that
\[
                 r_e+L_er_e^2<\tfrac12c_e(1-\cos a).
 \tag{8}
\]
For \(|t|\ge a\), (7),(8) imply (4) with coefficient \(c_e/2\).
Thus one may take \(\gamma_e=\min(a_e^*,c_e/2)\).

For the normal derivative fix the complex \(u\). On the real
spectral interval \([-2\cos(r/2),2]\), (4) bounds the polynomial
by \(CN^d\exp N\{\Re\psi(0,u)-\gamma_e(1-\cos(r/2))\}\).
Markov's inequality on this fixed interval gives its derivative
with an additional factor \(C_rD^2\). Restricting to
\([-2\cos r,2]\) gives the assertion, including the endpoint
\(t=\pi\). Markov applies to complex coefficients by rotating the
derivative at the point in question and applying the real inequality
to its real part. This proves the stated uniformity in complex \(u\).
\(\square\)

The different estimate needed on the deformed central contour retains
the outside *real* angular loss.

**Lemma 2 (full central kernel).** There are \(r_w,\gamma_w>0\)
such that
\[
 |K_N(t,u)|\le CN^d
 e^{N\{\Re\psi(t,0)-\gamma_w(1-\cos u)\}},
 \quad |t|\le r_w,\quad u\in[-\pi,\pi].
 \tag{9}
\]

*Proof.* On the retained wire interval \(I=[1/5,3/10]\),
[the weighted edge-contour estimate](research_weighted_edge_contour_bound.md)
gives (9) with coefficient \(1/20\). The complementary full
polynomial \(E_N=K_N-K_{N,I}\) has degree at most \(D\) in each
spectral variable and satisfies
\[
 \sup_{t,u\in[-\pi,\pi]}|E_N(t,u)|
                 \le CN^d e^{N(M_\infty-\delta_e)},
                 \qquad\delta_e=\pi/100.
 \tag{10}
\]
This is the original full Hermite wire bound, before any trace.
For fixed real \(u\), polynomial continuation in \(t\) changes
the rate by at most \(|\Im t|\). Since
\(|\psi(t,0)-M_\infty|\le L_e|t|^2\), choose \(r_w>0\)
inside the weighted-edge chart with
\[
                         r_w+L_er_w^2\le\delta_e/2.
 \tag{11}
\]
Then \(|E_N|\le CN^d e^{N\{\Re\psi(t,0)-\delta_e/2\}}\).
As \(1-\cos u\le2\), this implies (9) for the omitted indices
with coefficient \(\delta_e/4\). Adding the retained part proves
the lemma with \(\gamma_w=\min(1/20,\delta_e/4)\).
\(\square\)

## 2. Exact sources and the invariant data

Start with the complete terminal sources
\[
                    F_{0,N}(u)=H_{a,N}(u)=T(R^a)(-2\cos u),
                    \qquad |a|\ge2.
 \tag{12}
\]
For a word of fixed signed powers \(b_1,\ldots,b_k\), define
recursively in the original Hermite quotient
\[
 F_{\ell,N}(u)=T(R^{b_\ell}F_{\ell-1,N})(-2\cos u)
   =\phi_N^{(t)}\!\left[R^{b_\ell}F_{\ell-1,N}(t)K_N(t,u)\right].
 \tag{13}
\]
Every crossing, turn and edge in (13) is the original one. In
particular the crossing is not replaced by a Gaussian away from its
physical jets until the exact trace identity is applied.

We choose fixed constants \(R,H,a_0,c,C,h\) so that all constructed
sources have
\[
 F_N(u)=\varepsilon_N A(u)e^{NW(u)}(1+O_F(N^{-1})),
 \quad |\varepsilon_N|=1,
 \tag{14}
\]
on a neighborhood of \(|u|\le2R\), with a nonzero holomorphic
amplitude there, and
\[
 |W(u)-W(0)|\le H,\qquad \Re[-W''(u)]\ge a_0>0
                           \quad(|u|\le2R).
 \tag{15}
\]
The full polynomial has the global estimate
\[
 |F_N(x+iy)|\le C_FN^{d_F}
 e^{N\{M-c(1-\cos x)+Cy^2\}},
 \quad M=\Re W(0),\quad |x|\le\pi,\ |y|\le h.
 \tag{16}
\]
Only the prefactors, errors and starting levels depend on the word.

Here is a noncircular choice of the data. Choose \(R>0\) with
\(2R<r_e\), inside the common full terminal and zero-free amplitude
disk, and inside the fixed edge bidisk (5). Shrink it once so the
terminal actions satisfy \(\Re[-W_a'']\ge a_T>0\) there. The
[uniform terminal-family theorem](research_uniform_terminal_family_and_star_fillings.md)
justifies these choices for every \(|a|\ge2\). Set
\[
 a_0=\min(a_T,a_e^*),\qquad
 L_u=\sup\left|\frac{\psi_u(t,u)}u\right|,
 \quad
 H\ge\max\left(\sup_{|a|\ge2,|u|\le2R}|W_a(u)-W_a(0)|,
                                      2L_uR^2\right).
 \tag{17}
\]
The edge supremum is taken on the fixed bidisk and its quotient at
zero is removable. All constants are finite before the length or
powers of the word are chosen.

The proof below produces the real output coefficient
\(c_{r}=\min(c_e,\gamma_w)>0\), independently of the input
coefficient \(c\). The uniform phase bounds (15) then determine
constants \(c,C,h\) in (16), as explained in Section 5. Choose them
once to include the starting terminal family. No later choice of the
power threshold enters these strip constants.

## 3. A uniform power threshold

Fix \(0<r<\min(R/2,r_w/2)\). Cauchy's inequality applied to
(15) bounds \(|W''(t)|\le2H/R^2\) for \(|t|\le R\).
Choose \(L\) larger than this bound plus the fixed bound for
\(|\psi_{tt}(t,u)|\) on \(|t|\le R,|u|\le2R\). Then
\[
 \Phi(t,u)=W(t)+\psi(t,u),\qquad
 |\Phi_{tt}|\le L,\qquad \Re\Phi_{tt}\le-a_0
 \tag{18}
\]
on that rectangle for every admissible input.
Put
\[
 C_h=8\pi^2L,\qquad
 \delta=\min(\gamma_e,c_e)(1-\cos(r/2)).
 \tag{19}
\]
Choose a single integer \(B_*\) so that every \(|b|\ge B_*\)
satisfies
\[
 |b|>8\pi L,\quad |b|>16\pi/r,\quad
 \frac{C_h}{2b^2}<\min(\delta/4,a_0r^2/8),\quad
 \frac{C_h}{b^2}<r/4.
 \tag{20}
\]
Increase it if necessary to keep the whole midpoint rectangle in
\(|t|<\min(R,r_w)\). These choices depend only on the invariant
data and the bare edge.

The contraction proof in Section 3 of the one-step theorem now
applies for *every* complex \(|u|\le2R\). It gives the whole
charge path
\[
 t_\lambda=\frac{2\pi}{b}\{\lambda+i\Phi_t(t_\lambda,u)\},
 \qquad |t_\lambda|\le4\pi\lambda/|b|<r/4,
 \tag{21}
\]
with positive lower depth satisfying
\[
 \frac{2\pi^2a_0\lambda}{b^2}
 <-\Im t_\lambda<\frac{C_h\lambda}{b^2}.
 \tag{22}
\]
The selected action is
\[
 S(u)=\Phi(t_*(u),u)+\frac{ib}{4\pi}t_*(u)^2-it_*(u).
 \tag{23}
\]
Integration along the charge gives the comparison on the entire
unchanged disk:
\[
 0<\Re\{W(0)+\psi(0,u)-S(u)\}<\frac{C_h}{2b^2}.
 \tag{24}
\]

## 4. The full boundary expansion on the unchanged disk

Choose the physical midpoint \(r_N\ge r\),
\(r_N-r=O(N^{-1})\). For the outer original trace nodes
\(|t|\ge r_N\), use (4) with the same complex \(u\), and
\(|F_N(t)|\le C_FN^{d_F}e^{NM}\) from (16). Markov's
inequality on \([-2\cos(r/2),2]\) bounds the first normal of
the product with the same exponent and a polynomial cost. Thus
the entire outer trace has rate at most
\[
                   M+\Re\psi(0,u)-\delta.
 \tag{25}
\]
The original values and first normals of the fixed crossing power
only add polynomial factors. By (20),(24), (25) lies uniformly
below \(\Re S(u)\) throughout \(|u|\le2R\). This is the step
that avoids shrinking the outside disk. No expansion of the input
source is used at these outer nodes.

For the central nodes apply the exact identity (23) of the one-step
note to the *full* product \(F_N(t)K_N(t,u)\). The full edge
expansion (2) is valid on this rectangle, so no wire truncation
is needed. The depth is \(-\Im t_*(u)>0\). On its lower side
the phase has strictly negative real second derivative by (18),
and its derivative vanishes at \(t_*\). The horizontal maximum
is therefore unique. At the real endpoints, evenness gives the
loss \(a_0r^2/2\) relative to \(\Re\Phi(0,u)\); at the lower
endpoints strict concavity gives a fixed loss from \(\Re S(u)\).
After folding the two halves of the original endpoint current,
convexity in its vertical parameter bounds it by those endpoint
values. Equation (20) preserves both gaps. Every higher trace
charge has the factor \(O(e^{-N(-\Im t_*)})\); it is retained
and exponentially smaller for each fixed power and word.

The resulting Gaussian expansion is
\[
 F_{\rm new,N}(u)=\varepsilon_N C_{N,b}
      A_{\rm new}(u)e^{NS(u)}(1+O_{F,b}(N^{-1})),
 \tag{26}
\]
where
\[
 A_{\rm new}(u)=i\sqrt{\frac2\pi}
 \frac{\sin t_*(u)A(t_*(u))a_e(t_*(u),u)}
 {\sqrt{-W''(t_*(u))-\psi_{tt}(t_*(u),u)-ib/(2\pi)}}.
 \tag{27}
\]
The input amplitude is sampled only in \(|t|<r/4\), strictly
inside its fixed zero-free disk. The edge amplitude is also
nonzero. Equations (21),(22) imply \(0<|t_*|<r/4\), and
the real part of the negative Hessian is positive. Every factor
in (27) is therefore nonzero on the unchanged outside disk.
All estimates were made with strict margins inside the fixed
edge charts; they hold on a neighborhood of the closed disk.

The powers of \(N\) remain \(N^0\): the input has that power,
the edge contributes \(N^{-3/2}\), the trace \(N^2\), and
the Gaussian \(N^{-1/2}\). More generally the step preserves
any input power \(N^\alpha\). Its exact new carrier is only
\(C_{N,b}\), in addition to the already present input carrier.

## 5. Resetting the phase and global estimates

The envelope identity
\[
                             S'(u)=\psi_u(t_*(u),u)
 \tag{28}
\]
gives \(|S(u)-S(0)|\le L_u|u|^2/2\le2L_uR^2\), hence
the bound \(H\) in (17), with no accumulation from previous
turns.

The real curvature on the entire complex disk follows from the
exact Schur complement, not just its value at zero. Set
\[
 \mathcal H=-\begin{pmatrix}
  W''+\psi_{tt}+ib/(2\pi)&\psi_{tu}\\
  \psi_{ut}&\psi_{uu}
 \end{pmatrix}
 \tag{29}
\]
at \((t_*(u),u)\). Its Hermitian real part is at least
\(a_e^*I\): the edge supplies (5), the child supplies an
additional nonnegative central term, and the signed chirp is
purely imaginary. For a scalar \(v\), put
\(w=(-\mathcal H_{11}^{-1}\mathcal H_{12}v,v)\). Then
\[
 \Re\bigl(\overline v[-S''(u)]v\bigr)
      =\Re(w^*\mathcal H w)\ge a_e^*|v|^2.
 \tag{30}
\]
This proves the second bound in (15), with the same \(a_0\).

For every real outside angle use Lemma 2 on the central horizontal
segment and its full endpoint current. It gives the extra loss
\(\gamma_w(1-\cos u)\) relative to their already proved
complete-parent rates. For the outer real trace nodes use (3),
again with the crude bound \(|F_N(t)|\le C_FN^{d_F}e^{NM}\).
The normal derivative retains the losses on the fixed outer
spectral interval. Their rate is at most
\[
 M+M_\infty-c_e(1-\cos(r/2))-c_e(1-\cos u)
           \le\Re S(0)-c_e(1-\cos u)-3\delta/4.
 \tag{31}
\]
Thus the new full real-angle bound has the coefficient
\[
                           c_r=\min(c_e,\gamma_w),
 \tag{32}
\]
independent of the input coefficient, cutoff, or word length.

Here are fixed choices for the strip constants in (16). Cauchy's
inequality on the fixed disk gives \(|W''|\le L_2=2H/R^2\)
on \(|u|\le R\). For small real \(x,y\), (15), evenness,
Taylor's formula and Young's inequality give
\[
 \Re W(x+iy)\le M-\tfrac14a_0x^2+
                     (L_2^2/a_0+L_2/2)y^2.
 \tag{33}
\]
This applies uniformly both to the input family and to every new
phase. Away from \(|x|<R/2\), apply (27) of the one-step note
with coefficient \(c_r\). Its extra linear strip cost is at
most \((1+c_r)|y|\), whereas the real loss is at least
\(c_r(1-\cos(R/2))\). Choose one positive strip width small
enough to absorb half that gap, and also small enough that
\(|x|\le R/2\) lies in the local disk for those \(y\).
Taking, for example, \(c\le\min(c_r/2,a_0/4)\), and increasing
the common quadratic constant to cover (33), proves (16).
Finally reduce \(c,h\) and increase \(C\) to include the
initial uniform terminal family. These choices use only
\(R,H,a_0,c_r\) and the initial family; they are independent
of the word length and powers. This completes the noncircular
choice promised after (17).

## 6. The resulting word theorem and its scope

**Theorem.** There is a single integer \(B_*\) such that, for
every fixed length \(k\ge0\), every fixed \(|a|\ge2\), and
every fixed signed list \(|b_\ell|\ge B_*\), the original
boundary word
\[
       T\bigl(R^{b_k}T(R^{b_{k-1}}\cdots T(R^{b_1}T(R^a))\cdots)\bigr)
 \tag{34}
\]
has the nonzero full boundary expansion (14) and the common
estimates (15)--(16) on the same disk and strip. The phase is
obtained by the stationary construction (23) at each step.
The amplitude is obtained by (27), and the unit scalar is
\(\varepsilon_{a,N}\prod_{\ell=1}^k C_{N,b_\ell}\).
Every original first normal is retained. The theorem follows by
induction from Sections 2--5 and the uniform terminal theorem.

The uniformity concerns the eligibility threshold and analytic
domains. The constants in the relative asymptotic, the minimum
level needed for its validity, and the amplitude size may depend
on the entire fixed word. In particular this is not a bound
uniform in a length growing with \(N\).

For the original marked pieces, the geometric induction is the
one-child case of
[the recursive marked-block construction](research_recursive_marked_block_geometry.md).
The [large-power marked turn note](research_large_power_turn_marked_geometry.md)
spells out the one-step primitive periods and absolute volume anchor.
Choose the initial closed disk strictly inside its common terminal and bare-edge
charts. Equations (21)--(22) then keep the whole new charge path
in the inner child disk. All previously filled primitive slopes
remain fixed, the new original carrier occurs once, and the
outside longitude remains \(2iu\). This supplies the marked
geometric interpretation for these original compositions under
the same knot and framing conventions as that construction.
It does not require a lower bound on the lengths of previously
filled cores independent of the word.

This result allows arbitrary signs and arbitrarily many turns,
but it still assumes every noninitial power is long. It does
not prove cofinite coverage of arbitrary fixed templates, and
does not settle all pairs \((a,b)\) with \(|a|,|b|\ge2\).
In particular it does not assert closure under a short turn
or under arbitrary multiplication followed by a turn: the
exact cancellation counterexample in Section 7 of the one-step
note still applies outside these uniform hypotheses.

## 7. Closing the chain and the volume limit

The last step of an original circle-tree contraction has no outgoing
edge. For any boundary word just constructed, its exact scalar source is
\[
                       Z_N=\phi_N(R^{c_0}F_{k,N}),
 \tag{35}
\]
where \(c_0\) is the fixed signed closing power. The subscript
distinguishes it from the positive angular constant \(c\) in (16).
There is a single threshold \(B_{\rm cl}\), independent of the
preceding word, for which the whole original trace has a nonzero
asymptotic whenever \(|c_0|\ge B_{\rm cl}\).

Here are explicit sufficient conditions in the common constants.
Use the same real midpoint cutoff \(r\), let
\[
 L_{\rm cl}=2H/R^2,\qquad C_{\rm cl}=8\pi^2L_{\rm cl},\qquad
 \delta_{\rm cl}=c(1-\cos(r/2))>0,
\]
and require
\[
 |c_0|>8\pi L_{\rm cl},\quad |c_0|>16\pi/r,
 \quad
 \frac{C_{\rm cl}}{2c_0^2}
       <\min(\delta_{\rm cl}/4,a_0r^2/8),\quad
 \frac{C_{\rm cl}}{c_0^2}<r/4.
 \tag{36}
\]
The contraction (21) with \(\Phi=W_k\) gives a unique small
critical point \(s_*\) of
\[
                 W_k(s)+\frac{ic_0}{4\pi}s^2-is.
 \tag{37}
\]
The charge path satisfies the same positive lower-depth bounds.
Its rate loss from \(\Re W_k(0)\) is less than
\(C_{\rm cl}/(2c_0^2)\).

At the outer original trace nodes, (16) and Markov's inequality
retain the fixed gap \(\delta_{\rm cl}\), including the first
normals. Inside the midpoint rectangle the input packet (14)
has strictly negative real second derivative; its endpoint
currents are bounded by vertical convexity exactly as in Section 4.
The rational trace kernel retains and suppresses every higher
charge at the positive selected depth. Thus the exact original
trace, rather than a selected formal integral, gives
\[
 Z_N=\varepsilon_{k,N}C_{N,c_0}N^{3/2}
     D\,e^{N\mathcal V}(1+O_{\rm word}(N^{-1})),
 \tag{38}
\]
where
\[
 \mathcal V=W_k(s_*)+\frac{ic_0}{4\pi}s_*^2-is_*,
 \qquad
 D=i\sqrt{\frac2\pi}
       \frac{\sin s_*\,A_k(s_*)}
       {\sqrt{-W_k''(s_*)-ic_0/(2\pi)}}\ne0.
 \tag{39}
\]
There is no edge factor \(N^{-3/2}\) in this last trace, so the
normalization is \(N^2N^{-1/2}=N^{3/2}\). This also covers
\(k=0\), when the chain consists of the initial terminal piece
and this final filling.

Choose one integer
\(B=\max(B_*,B_{\rm cl})\), increasing it if needed for the
initial geometric charts. Consider any fixed original marked
circle-tree path, with the disk frames, half-twist parity pattern,
strand orientations and reduced cut of the circle-tree construction.
At each vertex the power is the original \(n_v=\eta_v-2p_v\),
and the filled primitive curve is \(\mu_v+p_v\lambda_v\).
Require that the literal strand tracing gives one main knot component
and no internal closed component. Let the initial terminal power
satisfy \(|a|\ge2\), and let every later power, including the
closing one, have magnitude at least \(B\). All these powers
are fixed before \(N\) tends to infinity; their signs and relative
magnitudes are independent.

The geometric induction in Section 6, followed by its final-root
version without an outgoing edge, constructs the complete positive
marked geometry. The old primitive filled slopes remain fixed
throughout the final charge path. Its initial absolute action is
\(W_k(0)\), and Schläfli's formula with the original once-only
closing carrier gives
\[
                     2\pi\Re\mathcal V
                        =\operatorname{Vol}(S^3\setminus K).
 \tag{40}
\]
The original reduced zero-framed Kashaev invariant is (35) times
the prescribed writhe unit. Consequently (38) becomes
\[
 \langle K\rangle_N=\Omega_N N^{3/2}D\,e^{N\mathcal V}
                 (1+O_K(N^{-1})),\qquad |\Omega_N|=1,
 \tag{41}
\]
through all sufficiently large integer levels, with both parities
and all the original normals retained. In particular
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|\langle K\rangle_N|
                     =\operatorname{Vol}(S^3\setminus K).
 \tag{42}
\]
The same \(B\) works for every fixed length of these paths and
every allowed initial terminal power. The result still leaves
infinitely many assignments outside its hypotheses: any noninitial
power may remain short while other powers grow. It therefore does
not assert the cofinite-template conclusion sought in the broader
research program.
