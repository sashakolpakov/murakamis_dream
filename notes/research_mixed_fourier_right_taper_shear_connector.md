# The complete right shear connector on the incoming taper

Research deduction, 7 November 2026. The negative retained path
introduced by the exact right-period identity has a calibrated bound
through the full nonpositive incoming right taper. Its comparison with
the left outgoing taper is independent of the incoming parameter.
Combining that comparison with the extended main sheet and the
transported real cuts avoids a direct real-direction loss on the
negative path.

The result bounds the actual infinite connector, and consequently
the complete upper-plus-positive-side retained group. Its baseline
is an explicit maximum of two original planes. The remaining
comparison with the compensated right-boundary tangent is retained;
it is not assigned a sign.

## 1. Original parameters, planes and finite source

Keep an original correlated reference
\((s_*,a_*,q_*)\), the output \(y=x_0=\xi+i\upsilon\), and
the allocation \(\eta\in\{0,1\}\) of
[the complete bare inner source](research_mixed_fourier_right_cap_bare_inner_completion.md).
We restrict to the references with
\[
 c=\Im a_*\in[-.108,0],\qquad
 h_s=\Im s_*,\ h_q=\Im q_*\in[-.102,-.001].
 \tag{1}
\]
Thus every incoming type-four reference is included, as is the
nonpositive-height part of the incoming type-three family. The new
incoming target is
\[
 a=x+ih,\qquad b=9/20,\quad b\le x\le1/2,\quad c\le h\le0.
 \tag{2}
\]
In particular (2) includes \(h=400(.5-x)^2c\). No new critical
point at this target is selected.

Write \(a_R=\Re a_*\), \(p_\eta=\Re P_\eta\), where
\(P_\eta=F_{\eta,a}(s_*,a_*,q_*)\), and let
\(M_\eta=\Re F_\eta(s_*,a_*,q_*)\). Set
\[
\begin{split}
 \kappa&=1/2500000,\qquad
 \chi_0=1989/4489,\quad\chi_1=171/196,\\
 B_\eta(b)&=M_\eta+p_\eta(b-a_R)-\kappa(b-a_R)^2,\\
 B_\eta^{\rm ext}(x)
   &=M_\eta+p_\eta(x-a_R)-\kappa\chi_\eta(x-a_R)^2,\\
 \gamma_\eta(x,h)&=\pi(1-\eta/2)(.5-x)(h-c),\\
 \mathfrak B_\eta(x,h)
   &=\max\{B_\eta(b),B_\eta^{\rm ext}(x)\}
                                  -\gamma_\eta(x,h).
\end{split}
 \tag{3}
\]
The coefficients \(\chi_\eta\) are the proved initial-segment
curvature reserves of
[the half-incoming sheet](research_mixed_fourier_right_cap_half_incoming_sheet.md).

Use the literal joint chart
\[
\begin{split}
 T_N(s,q;a)&=e^{2\pi iNas}\Pi_N(s+a)\Pi_N(s+q)
                    E_N(a)E_N(q)E_N(s)^3\widehat f_N(q;y),\\
 \widehat f_N(q;y)&=
 \frac{e^{-\pi i(N-1)y}}N e^{2\pi iNyq}
                       \Pi_N(1-y-1/N)E_N(q-y),
 \qquad E_N=1/\Pi_N
\end{split}
 \tag{4}
\]
with its original holomorphic reciprocal continuation. Its
allocated phase is
\[
 F_\eta(s,a,q)=g(s+a)+g(s+q)-3g(s)
       -(1+\eta/2)g(a)-g(q)+2\pi ias+\ell_q(y).
 \tag{5}
\]
The incoming factor \(|d_N(e^{-2\pi ia})|^{\eta/2}\) multiplies
every finite bound below; it is never divided out.
The cardinal \(1/N\) remains in (4), and there is no new
crossing scalar.

## 2. Both replacement paths have a paid real seam

Let \(\Psi_\eta(s,a)=F_\eta(s,a,0)\), with \(g(0)=0\).
The already proved outgoing taper comparison is
\[
 \Re\Psi_\eta(u+iv,a)
 <\Re F_\eta(u+iv,a,11/50+ih_q)-3/400,
 \quad 1/8\le u\le1/2,\quad h_s\le v\le0.
 \tag{6}
\]
Although its original application had \(\Re a\in P\), its proof
applies unchanged to (2): the directional derivative \(F_{\eta,q}\)
and the difference in (6) contain no \(a\). The certified two-function
inequality and its first-hundredth reserve in
[the left-taper completion](research_mixed_fourier_left_taper_source_completion.md),
Sections 1--3, therefore establish (6) without a new evaluation.
This is a difference of original lifted phases, not a comparison
of unrelated stationary branches.

First work at incoming height \(c\). On \(v=h_s\), the extended
sheet gives
\[
 \Re F_\eta(u+ih_s,x+ic,11/50+ih_q)
                       \le B_\eta^{\rm ext}(x).
 \tag{7}
\]
At either real retained cut \(u=1/8,1/2\), the positive-height
real-direction transport, which includes \(v=0\), gives
\[
\begin{split}
 \Re F_\eta(u,x+ic,11/50+ih_q)
 &\le \Re F_\eta(u,b+ic,11/50+ih_q)\\
 &<B_\eta(b)-1/35000 .
\end{split}
 \tag{8}
\]
Here the last inequality is the original completed individual
cut comparison. No bound on a canceled sum is subtracted.

For the side joins between \(h_s\) and zero, the vertical convexity
used in (7)--(8) persists at \(x\in[b,.5]\). Indeed, throughout
this height interval the decomposition
\[
 F_\eta=V(s,a)+\{V(s,q)-g(s)\}
                     -\eta g(a)/2+2\pi ias+\ell_q(y)
 \tag{9}
\]
has the same nonnegative negative-real Hessian as in the
half-incoming-sheet proof. The new pair has
\(\Re\cot\pi s,\Re\cot\pi a\ge0\) and
\(\Re\cot\pi(s+a)\le0\). The old \((s,q)\) pair is positive
for \(u\ge.15\); at the left cut the unchanged
\(\lambda=1\) Schur bound is \(13/24\), on the entire old
height strip, including \(h_s\le v\le0\).
Thus \(\partial_v^2\Re F_\eta=-\Re F_{\eta,ss}\ge0\).
At \(s=a=.5\) with zero total height, take the continuous
one-sided limit of this convexity statement; the numerator
factorial has a zero there, not a pole.
The endpoints (7)--(8), followed by (6), bound the whole
negative path by
\[
 \max\{B_\eta(b),B_\eta^{\rm ext}(x)\}-3/400.
 \tag{10}
\]

The positive path is even simpler. Let \(\Gamma(5/4)\) be
the oriented path from \(1/8\) vertically to \(1/8+5i/4\),
then to \(1/2+5i/4\), then down to \(1/2\). The old real-seam
proof bounds each point, with its actual upper Fourier debit, by
\[
 \Re\Psi_\eta(s,b+ic)-2\pi\Im s<B_\eta(b)-3/400.
 \tag{11}
\]
Lemma 2 of
[the all-height incoming transport](research_mixed_fourier_incoming_taper_all_height.md)
moves this pointwise inequality to \(x+ic\), since every retained
height on this path is nonnegative. Lemma 1 of the same note
then raises \(c\) to \(h\) on both paths, paying the common
nonnegative credit \(\gamma_\eta(x,h)\).
Consequently the limiting paths \(\Gamma(5/4)\) and
\(\Lambda(h_s)\), the latter going down to height \(h_s\)
and returning, satisfy
\[
\begin{split}
 \Re\Psi_\eta(s,a)-2\pi\Im s
       &<\mathfrak B_\eta(x,h)-3/400
                                     &&(s\in\Gamma(5/4)),\\
 \Re\Psi_\eta(s,a)
       &<\mathfrak B_\eta(x,h)-3/400
                                     &&(s\in\Lambda(h_s)).
\end{split}
 \tag{12}
\]
In the second line there is no retained Fourier debit.

These seam bounds refer to the literal physical \(q=0\) source.
At the actual half-grid cuts and for \(\alpha_N\le q\le0\),
\(\alpha_N=-1/(2N)\), its interpolation is still (4).
The exact seam proof, Section 5, supplies
\(|E_N(q)|\le C\) by an undivided finite product and a regular
denominator. The shared-factor ratio
\(\Pi_N(s+q)/\Pi_N(s)\) and the cardinal normalization relative
to \(f_0(y)\) are uniformly bounded on these compact retained
paths. The incoming numerator is handled by the zero-safe
bound discussed below. Hence each of the profiles in (12)
continues to this shrinking real segment with a uniform
polynomial prefactor and an arbitrarily small rate tolerance.
This statement concerns these central contour profiles; it
does not assert a new estimate for the omitted physical low rows.

## 3. The exact right-period connector and its compact bound

Put \(M_N=\lceil N/2\rceil-1\), \(L_N=\lceil N/8\rceil\),
\(\sigma_-=(L_N-\tfrac12)/N\), \(\sigma_+=(M_N+\tfrac12)/N\).
Use these actual cuts in both paths from now on. Let
\[
\begin{gathered}
 \beta_N=1+\alpha_N,\quad q_L(t)=\alpha_N+i(h_q-t),
 \quad q_R(t)=1+q_L(t),\quad t\ge0,\\
 Z_q=e^{-2\pi iNq_L(t)},\quad
 R_q=\frac{Y^N}{1-Y^NZ_q},\quad A_q=\frac{Z_q}{1-Z_q},
 \quad k_N^+(s)=\frac{e^{2\pi iNs}}{1-e^{2\pi iNs}} .
\end{gathered}
 \tag{13}
\]
The exact original period identity is unchanged:
\[
 k_N^+(s)T_N(s,q_R)
          =R_q\{k_N^+(s)T_N(s,q_L)-A_qT_N(s,q_L)\}.
 \tag{14}
\]
For any \(0<b_0<-h_q\), the complete right connector is therefore
\[
\begin{split}
 Q_{R,N}(T)
 &=N^2\int_0^T\int_{\Gamma(b_0)+it}
                    k_N^+(s)T_N(s,q_R(t);a)\,ds\,dt\\
 &=N^2\int_0^T R_q\left[
       \int_{\Gamma(5/4)+it}k_N^+(s)T_N(s,q_L(t);a)\,ds
       -A_q\int_{\Lambda(h_s)+it}T_N(s,q_L(t);a)\,ds
                            \right]dt .
\end{split}
 \tag{15}
\]
This is the same oriented identity as
[the original right connector](research_mixed_fourier_right_endpoint_shear_comparison.md),
equation (7). The incoming change creates no new pole:
\(\Pi_N(s+a)\) is a numerator holomorphic at \(s+a=1\).
The shared real part \(s+q_L\) remains in \((0,1)\);
the upper kernel has no pole between the two positive paths,
and the second path carries no retained kernel. The two
terms in (15) cannot be separated before this exact replacement.

At limiting \(q_L(0)=ih_q\), the right cardinal factor pays
the same incoming-independent comparison as before:
\[
 \Re F_\eta(s,a,ih_q)-2\pi\upsilon
 <\Re\Psi_\eta(s,a)
           +(\pi+\phi)|h_q|-2\pi\upsilon
 <\Re\Psi_\eta(s,a)-1/50 .
 \tag{16}
\]
This is the all-retained-height comparison in the
[vertical-current completion](research_mixed_fourier_right_cap_vertical_current_completion.md),
equation (24). It involves only \(s,q,y\), so (2) does not
alter its proof.

The possible subsequent increase is still less than \(1/80\).
For \(s_t=u+i(v_0+t)\), \(q_t=i(h_q-t)\), write
\(H=v_0+t\), \(r=e^{-2\pi H}\), \(R=e^{2\pi(h_q-t)}\).
The exact paid derivative is
\[
\begin{split}
 -\frac d{dt}\{\Re F_\eta(s_t,a,q_t)-2\pi(v_0+t)\}
   ={}&4\pi u-\phi+3A_r(u)\\
      &-A_{r e^{-2\pi h}}(u+x)+A_{\rho R}(-\xi).
\end{split}
 \tag{17}
\]
Here \(A_R(w)=\Arg(1-Re^{-2\pi iw})\) has its original
regular-strip lift. Now \(.575\le u+x\le1\), so the
incident argument in (17) is nonpositive at every radius.
It only improves the old estimates. For \(H\ge0\),
\(4\pi u+3A_r(u)\ge\pi/2\), giving the lower bound
\(2/5-(7/10)e^{-2\pi t}\). For \(H<0\),
\(4\pi u+3A_r(u)\ge13\pi/8\), so the old lower bound
greater than two also remains valid. Integrating the positive
part of the resulting upper derivative gives exactly
\[
 \frac1{2\pi}\{3/10-(2/5)\log(7/4)\}<1/80 .
 \tag{18}
\]
At \(u=x=.5\) the integrated statement follows by the continuous
factorial limit; no derivative at its isolated zero is used.

For the first term of (15), combine (12), (16) and (18)
with its retained debit. For the second, the exact \(A_q\)
has rate \(2\pi(h_q-t)\); its variation is the same
\(-2\pi t\), and its additional starting term \(2\pi h_q\)
is negative. Thus both replaced profiles have rate at most
\[
 \mathfrak B_\eta(x,h)-3/400-1/50+1/80
                         =\mathfrak B_\eta(x,h)-3/200 .
 \tag{19}
\]

For every fixed \(T\), this is a uniform finite-source bound
on \(0\le t\le T\), up to a polynomial and an arbitrary fixed
rate tolerance. The only newly encountered compact wall is
\(s+a=1\). The undivided quarter-\(N\) shift from the all-height
note, equations (14)--(16), gives
\[
 |\Pi_N(w)|\le C_TN^{A_T}e^{N\Re g(w)},
       \qquad 11/20\le\Re w\le1,\quad|\Im w|\le T+2.
 \tag{20}
\]
It retains the numerator zero. All other arguments have their
old regular or lower-half-plane bounds, including \(q_L\) at
negative real part. The changes \(q_L(0):ih_q\mapsto
\alpha_N+ih_q\) and \(u:1/8,1/2\mapsto\sigma_\pm\) are uniformly
small in the continuous rate functions. At the numerator wall
we use uniform continuity and spare fixed rate tolerance,
not an unsupported bounded logarithmic derivative.
The exact kernel denominators in (13) have the same
uniform bounds as in the original connector proof.

## 4. Infinite ends and the assembled positive group

The offset factorial-tail lemma remains uniform on (2).
In its notation \(s_t=u+i(v_0+t)\), \(q_t=z+i(k_0-t)\),
allow \(v_0\in[-.2,5/4]\), \(k_0\in[-.102,-.001]\),
\(z\in[-.01,1]\), and \(u\in[.12,.5]\). For \(t\ge1\),
all moving lower-half-plane remainders have depth at least
\(t-.308\) and modulus at most \(t+3\), also when
\(\Re(s+a)=1\). These bounds used only \(|h|\le.108\)
and bounded real parts of the arguments; replacing the old
upper bound \(.95\) for \(\Re(s+a)\) by one preserves them.
The lower-half-plane exact factorial formula and reflection
hold there without a real-strip endpoint restriction.

The cancellation of all incoming real and height terms in the
tail slope is exact. For
\(\mathcal A_N(t)=e^{2\pi iNs_t}T_N(s_t,q_t;a)\),
the unchanged lemma gives
\[
 |\mathcal A_N(t)|
 \le |\mathcal A_N(T_1)|
       e^{12N\psi_{\rm off}(T_1)
                    -2\pi\{N(2u-\xi)+1\}(t-T_1)},\quad t\ge T_1,
 \tag{21}
\]
where \(\psi_{\rm off}(T_1)\downarrow0\) uniformly in (2).
The fixed shared numerator may vanish and is retained
multiplicatively; no comparison divides it.
For the second term of (15), keep the exact identity
\[
 Z_qT_N(s_t,q_t)=
          e^{-2\pi iN(s_t+q_t)}\mathcal A_N(t).
 \tag{22}
\]
Its first factor is constant along the shear and stays in
the bound at \(T_1\). All denominator ratios are uniformly
bounded, and \(|Y|^N\) is retained there too.

Choose \(T_1\) once so that \(12\psi_{\rm off}(T_1)<1/1000\).
Use (19) on its compact initial interval and at \(T_1\),
with a finite-source tolerance smaller than \(1/1000\).
Integrate (21) on the rest. Its slope is uniformly greater
than \(\pi N/10\) for large \(N\). At each smaller nonempty
level its exact positivity follows instead from
\[
 N(2u-\xi)+1\ge2\lceil N/8\rceil-N\xi
                         \ge N(1/4-\xi)>0.
 \tag{23}
\]
Thus absolute convergence at fixed level and the uniform
large-\(N\) estimate are separate justified statements.
Polynomial prefactors, both path lengths, the original
\(N^2\), and the sum of the two replaced terms are absorbed
by the reserve in (19).

**Theorem 1.** Uniformly on (1)--(2), for all sufficiently
large levels of either parity,
\[
 |d_N(e^{-2\pi ia})|^{\eta/2}N^2
 \int_0^\infty\left|
     \int_{\Gamma(b_0)+it}
          k_N^+(s)T_N(s,q_R(t);a)\,ds\right|dt
       \le e^{N(\mathfrak B_\eta(x,h)-1/200)} .
 \tag{24}
\]
The integral is absolutely convergent at each fixed level.
Its estimate takes the modulus after the exact complete-path
replacement (15); it does not bound the original small-arch
profiles separately.

There is also an immediate assembled consequence. Denote by
\(\mathcal I_N(0)\) the complete original upper-plus-positive-side
retained contribution on \(9/20\le\Re q\le\beta_N\), exactly as
in equation (17) of
[the original arch transport](research_mixed_fourier_original_upper_shear_transport.md).
The two retained faces start at height zero and the left outgoing
face uses the exact high-cap replacement. Every point of those
replacement surfaces has nonnegative retained height. Its original
phase, including its upper debit, is therefore bounded by its own
profile at incoming \(b+ic\), minus \(\gamma_\eta\).
The existing compact phase bounds and (20)--(21) give their
complete absolute bound with gap \(1/140000\) below
\(B_\eta(b)-\gamma_\eta\). This uses the already proved individual
profiles, not a modulus comparison of different finite sources.

The exact four-face identity and the vanishing far arch are
unchanged, because the new numerator wall introduces no pole.
Combining those three faces with (24) proves
\[
 \boxed{\qquad
 |d_N(e^{-2\pi ia})|^{\eta/2}|\mathcal I_N(0)|
          \le e^{N(\mathfrak B_\eta(x,h)-1/280000)} .
 \qquad}
 \tag{25}
\]
All original orientations, both retained side pieces, the
outgoing period multiplier, cardinal normalization and both
parity cuts remain in this group.

## 5. The original marginal is still required

Let
\(\mathcal L_\eta(a)=\Re\{\Pi_\eta^{\rm F}(a_*;x_0)
                                      +P_\eta(a-a_*)\}\).
The exact difference of the baseline in (24)--(25) from the
original complex tangent is
\[
\begin{split}
 \mathfrak B_\eta(x,h)-\mathcal L_\eta(x+ih)
 ={}&\Im P_\eta(h-c)-\gamma_\eta(x,h)\\
 &+\max\{-p_\eta(x-b)-\kappa(b-a_R)^2,\,
                         -\kappa\chi_\eta(x-a_R)^2\}.
\end{split}
 \tag{26}
\]
No sign is asserted for (26). It must be combined with the
adjacent ordinary allocation and the synthetic right extension.
In particular (25) closes the complete positive retained
correction group on the full incoming taper; it is not a
complete low-source or compensated boundary theorem there.
It also does not extend to selected incoming contours, positive
incoming heights, or an arbitrary output parameter.
