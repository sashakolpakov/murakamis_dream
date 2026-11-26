# Both private cap aliases are below the original horizontal line

Research deduction, 6 November 2026. The two horizontal aliases of
the first type-four cap are pointwise below its main private line,
uniformly over the full outgoing plateau at the selected height. The
proof uses the original canonical endpoint square root and fixes its
logarithmic lift explicitly. Consequently the six remaining cap-alias
profiles in the first-four/next-three reduction introduce no additional
comparison. Their reduction to cap-main profiles does not establish
the still-open ordinary real-cut comparisons.

## 1. The canonical private derivative

Keep
\[
 \begin{gathered}
 \mathcal E=[.27,.49]+i[-.055,.04],\qquad
 e=x+i\eta,\qquad z=y+ik,\\
 y\in P=[.22,.45],\quad 0\le k\le.014,\qquad
 -.051<h_e<-.019,\\
 \Psi(e,z)=S(e)+J(e+z)-J(z)-i\pi ez-g(e).
 \end{gathered}
\tag{1}
\]
Here \(h_e\) is the unchanged actual private height of the first
type-four endpoint. There is no moving cap critical point at the
outgoing target \(z\). The complete endpoint theorem on
[the private rectangle](research_mixed_endpoint_cap_rectangle.md)
gives the original canonical function \(u=u_c(e)\) and
\[
 .17<\Re u<.28,\quad \Im u>0,\qquad
             .01<\Re(e-u)<.32.
\tag{2}
\]
The sharper upper difference in (2) follows from
\(x\le.49\), \(\Re u>.17\); the lower difference is the
theorem's retained upper cut \(\Re u<x-.01\).

The same theorem defines
\(S(e)=F(e,u_c(e))\), with
\(F_e=-J'(e-u)+i\pi u\). Since \(F_u=0\) on the
original zero lift, conversion using
\(g'(w)=J'(w)+i\pi(1/2-w)\) gives the exact derivative
\[
 \Psi_e=g'(e+z)-g'(e)-g'(e-u)+2\pi iu.
\tag{3}
\]
All displayed arguments have real parts strictly between zero and
one. Set
\[
 E=e^{-2\pi ie},\quad V=e^{-2\pi iu},\quad Z=e^{-2\pi iz},
 \quad W=\sqrt{1-2/E},\quad D=iEW.
\tag{4}
\]
The square root \(W\) is exactly the one in the canonical
arctangent formula for \(u_c\), with positive real and negative
imaginary parts. It is not a new choice of a root.
Write \(E=r e^{-i\theta}\), where
\[
             .54\pi\le\theta\le.98\pi,
                    0<r<3/2.
\tag{5}
\]
For the radius, \(r\le e^{.08\pi}\),
\(.08\pi<13/50\), and
\(e^t\le(1-t)^{-1}\) for \(0\le t<1\) give
\(r<50/37<3/2\). Put \(W=a-ib\), with \(a,b>0\).
The imaginary part of \(D=iEW\) is
\(r(\cos\theta\,a-\sin\theta\,b)<0\).
Also
\[
 D^2=E(2-E),\qquad
 \Im D^2=2\Im E(1-\Re E)<0.
\tag{6}
\]
It follows that \(\Re D>0>\Im D\), throughout the connected
rectangle. In particular \(1-D\) is in the open upper half-plane.

The original arctangent formula gives
\[
 V=\frac{3-iW}{1+iW}
   =\frac{E+1-2D}{E-1},\qquad
             (1-E)(V-E)=-(1-D)^2.
\tag{7}
\]
These are the canonical identities already used in
[the private barrier proof, Section 9](research_mixed_selected_boundary_height_envelope.md).
Here the same algebra applies on the entire rectangle (1).
The denominators do not vanish: \(\Re E<0\),
\(\Re W>0\), and \(e-u\) remains in its regular strip.

We now fix the argument in (7), rather than only its exponential.
Use the original argument
\(\mathcal A(t,h)=\arg(1-e^{2\pi h-2\pi it})\).
For \(0<t<1\) and arbitrary finite \(h\),
\[
 \pi\min(1-2t,0)\le\mathcal A(t,h)
                      \le\pi\max(1-2t,0).
\tag{8}
\]
These are the radius-angle bounds in
[the ordinary alias proof](research_mixed_horizontal_alias_transport.md).
Put \(q=\Re u\) and
\[
 T=-\mathcal A(x,\eta)
       -\mathcal A(x-q,\eta-\Im u)+2\pi q.
\tag{9}
\]
Both arguments subtracted here are positive. Applying (8) and (2)
gives
\[
                   -.92\pi<T<.56\pi.
\tag{10}
\]
Indeed its lower bound is \(T>\pi(4x-2)\), and its
upper bound is \(T<2\pi q\). Let
\(\alpha=\Arg(1-D)\in(0,\pi)\). Equation (7) says that
\(T\) is congruent to \(\pi-2\alpha\) modulo \(2\pi\).
The latter belongs to \((-\pi,\pi)\), and (10) excludes
every nonzero multiple of \(2\pi\) for their difference.
Consequently the original lift of (3) is exactly
\[
       \Im\Psi_e(e,z)=\mathcal A(x+y,\eta+k)
                               +\pi-2\Arg(1-D).
\tag{11}
\]

## 2. A cap-angle bound on the whole rectangle

**Lemma 1.** Throughout (1),
\[
                 \Arg(1-D)<\pi-\theta/2=\pi(1-x).
\tag{12}
\]

*Proof.* Use the square root of \(2-E\) in the first quadrant.
With the sign already fixed in (6),
\(D=\sqrt r\,e^{-i\theta/2}\sqrt{2-E}\).
Thus
\[
 \Im\{(1-D)e^{i\theta/2}\}
       =\sin(\theta/2)-\sqrt r\,\Im\sqrt{2-E}.
\tag{13}
\]
Both terms being compared are positive. Squaring shows that (13)
is positive exactly when
\[
        r\{|2-E|-2+r\cos\theta\}<1-\cos\theta.
\tag{14}
\]
Rationalizing the braces and canceling the positive
\(1-\cos\theta\) reduces (14) to
\[
 r^3(1+\cos\theta)<|2-E|+2-r\cos\theta.
\tag{15}
\]
Its left side is less than \(27/8\) by (5); its right side
is at least \(4-2r\cos\theta>4\). This proves (14).
Since \(0<\Arg(1-D)<\pi\) and
\(0<\theta/2<\pi/2\), positivity in (13) forces their
sum to be less than \(\pi\). This is (12). \(\square\)

**Lemma 2.** The original private marginal satisfies
\[
 -\frac{9\pi}{10}<\Im\Psi_e<\frac{29\pi}{50}
                   \quad(e\in\mathcal E),\qquad
 \Im\Psi_e> -\frac{73\pi}{100}\quad(\eta\le0).
\tag{16}
\]

*Proof.* If \(x+y\ge1/2\), equations (8), (11)--(12)
give \(\Im\Psi_e>-2\pi y\ge-.9\pi\).
If \(x+y<1/2\), its argument is positive, so (11)--(12)
instead give \(\Im\Psi_e>\pi(2x-1)\ge-.46\pi\).
For the upper bound, use (3) and (9) directly. The two subtracted
arguments are positive, \(2\pi q<.56\pi\), and the
remaining argument is nonpositive unless \(x+y<1/2\).
In that exceptional small strip it is at most
\(\pi(1-2(x+y))\le.02\pi\). This proves the first pair
of inequalities in (16).

If \(\eta\le0\), then both \(e\) and \(e-u\) have
nonpositive imaginary parts, by (2). For a real part below one half,
the sharper unit-radius argument bound is
\(\mathcal A(t,h)\le\pi(1/2-t)\) when \(h\le0\).
It follows from (9) that \(T>\pi(2x+q-1)\).
When \(x+y\ge1/2\), adding its lower argument bound gives
\(\Im\Psi_e>\pi(q-2y)>-.73\pi\).
When \(x+y<1/2\), it gives instead
\(\Im\Psi_e>\pi(2x+q-1)>-.29\pi\).
This proves the last assertion. \(\square\)

## 3. Pointwise alias comparison and its finite consequence

**Proposition 3.** For every \(x\in[.27,.49]\) and all
parameters in (1),
\[
 \begin{split}
 \Re\Psi(x-.055i,z)-.11\pi
   &<\Re\Psi(x+ih_e,z)-\frac{557\pi}{6250},\\
 \Re\Psi(x+.04i,z)-.08\pi
   &<\Re\Psi(x+ih_e,z)-\frac{677\pi}{100000}.
 \end{split}
\tag{17}
\]
The two gaps exceed \(1/4\) and \(1/50\), respectively.

*Proof.* Holomorphy gives
\(\partial_\eta\Re\Psi=-\Im\Psi_e\).
The lower-alias increase over the same main-line real coordinate is
less than \((29\pi/50)(h_e+.055)<(.58)(.036)\pi\).
Subtracting its penalty \(.11\pi\) gives the first line.
For the upper alias, split the height integral at zero. Its increase
is less than
\[
 \frac{73\pi}{100}(-h_e)+\frac{9\pi}{10}(.04)
             <(.73)(.051)\pi+(.9)(.04)\pi=.07323\pi.
\tag{18}
\]
Its penalty is \(.08\pi\), giving the second line.
Finally \(\pi>3\) proves both stated rational lower gaps.
\(\square\)

In the five-profile notation of
[the finite first-four/next-three reduction](research_mixed_selected_four_three_finite_reduction.md),
taking the maximum in the *same* real coordinate gives
\[
          A_-<A_0-1/4,\qquad A_+<A_0-1/50.
\tag{19}
\]
These inequalities preserve the reference height, outgoing target and
both Fourier alternatives. Adding any of the ordinary profiles does
not change them. In particular alias times ordinary main is strictly
suppressed by the proved main-times-main gap. Alias times an ordinary
real cut is dominated by cap main times that **same** cut; no negative
sign for the latter is inferred.

The [last-row theorem](research_mixed_selected_four_three_last_rows.md)
already pays all five ordinary-last-row pairs. With
\(H=7/625\), define the remaining eight-profile defect by
\[
 \mathcal D_8(y,v)=
 \max_{\substack{i,j\in\{0,L,R\}\\(i,j)\ne(0,0)}}
 \max_{\sigma\in\{\mathrm{fac},\mathrm{force}\}}
 \{A_i(y)+B_j(y,v)+W_\sigma(y)-M-\ell_b(v)\}.
\tag{20}
\]
Equation (19), the complete finite reduction, the central comparison,
and the last-row theorem give
\[
 |\partial_w^k\mathcal K_N(w;X,Y)|
 \le C_{\tau,k}N^{D_{\tau,k}}
 e^{N\{M+\ell_b(v)+\max(-1/500,\mathcal D_8(y,v))+\tau\}}.
\tag{21}
\]
All factors and the original complete selected Fourier polynomial
remain literal. The original contour has fixed compact regular
factorial arguments. Its complete endpoint packet persists on a
fixed small ordinary-color disk, where an arbitrarily small total
rate tolerance absorbs the change from complete color. Half-grid
rounding and polynomial symbols use the same tolerance; Cauchy's
formula then gives each fixed ordinary-color derivative. Both level
parities remain covered. This invokes no new root or source check.

The pointwise cap statement also applies to a first type-four cap
followed by type four, since that next type does not enter (1)--(19).
The eight-profile reduction (21) uses the specifically proved
next-three central gap and makes no next-four central assertion.
Neither case supplies the missing real-cut signs or whole open-word
dominance.
