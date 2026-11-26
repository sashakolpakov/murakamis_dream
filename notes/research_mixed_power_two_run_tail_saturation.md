# Saturation of the Fourier lower-tail margin after one more power-two block

Research deduction, 7 November 2026. The exact source for three
consecutive power-two blocks retains the central Gaussian mechanism
of the two-block proof, but it saturates the lower outer sampling
debit. Its fixed-level lower alias still tends to zero. The absolute
row-majorant argument used for the two-block kernel, however, no
longer has a decay slope proportional to \(N\).

This is a limitation of that Fourier contour criterion, not an
uncovered same-sign cluster theorem. The original ordinary
two-boundary results for
[internal two-crossing chains](research_internal_two_crossing_chain.md)
and [all nonzero degree-two fillings](research_all_nonzero_degree_two_fillings.md)
already cover the corresponding same-sign runs. Their existing
coherent reduction and boundary adapters remain intact.
No numerical evaluation is used.

## 1. The complete original three-block source

Use
\[
 D=N-1,\quad r=e^{-2\pi i/N},\quad Q=r^{-1},\quad
 P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\quad
 \nu_j=(-1)^j e^{\pi i j(j+1)/N}.
 \tag{1}
\]
The full Fourier matrix for the known three-block run is
equation (14g) of
[the merged-source theorem](research_mixed_two_adjacent_merged_source.md):
\[
 B^{[3]}_{jk}=
 \begin{cases}
 P_j^3P_k^3/(N^2P_{j+k-D}),&j+k\ge D,\\
 0,&j+k<D,
 \end{cases}
 \qquad A_2^3=S^TB^{[3]}S.
 \tag{2}
\]
Retain its exact cardinal reversal
\[
 f_{D-u}(x)=\frac{e^{\pi iDx}}N\,\nu_u p_u(X),
 \qquad X=e^{-2\pi ix},
 \tag{3}
\]
and \(P_{D-u}=N/(\nu_uP_u)\). Reversing both indices in
\(f(x)^TB^{[3]}f(y)\) gives the complete identity
\[
 \boxed{\quad
 h(x)^TA_2^3h(y)
  =N e^{\pi iD(x+y)}
      \sum_{\substack{u,v\ge0\\u+v<N}}
       \frac{Q^{uv}\nu_u^{-1}\nu_v^{-1}
          P_{u+v}p_u(X)p_v(W)}{P_u^3P_v^3},
       \qquad W=e^{-2\pi iy}.
 \quad}
 \tag{4}
\]
For the scalar check, reversal gives
\(N\,\nu_{u+v}/(\nu_u^2\nu_v^2)\), and
\(\nu_{u+v}/(\nu_u\nu_v)=Q^{uv}\).
Thus the outside \(N\), the two inverse chirps, and
the full physical triangle are all original factors.

This run is already conjugate to a single signed crossing
power with its adapters:
\[
             A_2^3=\kappa^3M^{-1}JM^{-3}JM.
 \tag{5}
\]
Equation (5) is the known all-run identity, not a new
identification of arbitrary prescribed observations.

## 2. The exact central source and the preserved inner inequality

For physical \(a=u/N,s=v/N\), the inverse chirp is
\[
 \nu_u^{-1}
     =e^{\pi iN(a-a^2)-\pi ia}.
 \tag{6}
\]
Use this same original interpolation and define
\[
\begin{split}
 \mathscr T_{3,N}(a,s;x,y)={}&
 e^{2\pi iNas+\pi iN(a+s-a^2-s^2)-\pi i(a+s)}\\
 &\cdot\Pi_N(a+s)\Pi_N(a+x)\Pi_N(s+y)
                  E_N(a)^3E_N(s)^3E_N(x)E_N(y).
\end{split}
 \tag{7}
\]
It equals the summand in (4) at every supported physical
row. For a total \(c=a+s\), set
\[
 \mathcal H^{[3]}_{\sigma,N}(c;x)=
     \sum_{\substack{d\in\mathbb Z+\sigma\\|d|\le N/5}}
      \mathscr T_{3,N}(c/2+d/N,c/2-d/N;x,x).
 \tag{8}
\]
As before, this is an exact holomorphic finite central
source on the regular all-height chart. Its physical
parity choice retains precisely the original central
rows of (4).

Its original phase is
\[
\begin{split}
 F_3(a,s;x,y)={}&g(a+s)+g(a+x)+g(s+y)
        -3g(a)-3g(s)-g(x)-g(y)\\
       &+2\pi ias+\pi i(a+s-a^2-s^2).
\end{split}
 \tag{9}
\]
The additional finite symbol factor is \(e^{-\pi i(a+s)}\).
The regular row power is \(N^{-5/2}\).

At equal external endpoints and fixed total, the phase is
symmetric. Write \(a=c/2+t,s=c/2-t\), and use the squared
moduli \(N_\pm,D_\pm\) from section 2 of
[the all-height central theorem](research_mixed_two_adjacent_all_height_central_packet.md).
Then
\[
 \frac{d}{dt}\Re F_3(c/2+t,c/2-t;x,x)
       =\frac12\log\frac{N_+}{N_-}
                    -\frac32\log\frac{D_+}{D_-}.
 \tag{10}
\]
The extra chirps again have purely imaginary inner
derivative. On that theorem's actual external domain
\(S>1,\ S\cos(2\pi\Re x)<1\), for every finite total
height and \(1/2\le\Re c<1\), its exact ratio comparison
gives, for \(0<t\le1/5\),
\[
 \frac{d}{dt}\Re F_3
                  <-\log(D_+/D_-)<0 .
 \tag{11}
\]
The automatic case of a nonpositive shifted numerator
difference gives the same weaker inequality.
The left half follows by symmetry.

Thus the central maximum and its uniform compact
nondegeneracy survive this attachment. Explicitly the
reduced phase and inner Hessian are
\[
\begin{split}
 \phi_3(c,x)&=g(c)+2g(c/2+x)-6g(c/2)-2g(x)+\pi ic,\\
 \mathcal K_3(c,x)&=
       2\pi\cot\pi(c/2+x)-6\pi\cot(\pi c/2)-4\pi i,\\
 \Re\mathcal K_3(c,x)&\le-4\pi\Re\cot(\pi c/2)<0.
\end{split}
 \tag{12}
\]
The original symmetric finite Gaussian argument therefore
gives a nonzero complete central packet
\[
 \mathcal H^{[3]}_{\sigma,N}(c;x)
      =N^{-2}\mathcal A_3(c,x)e^{N\phi_3(c,x)}
                                       (1+O(N^{-1}))
 \tag{13}
\]
on fixed bounded-height compacts, for both parities,
where
\[
 \mathcal A_3(c,x)=
 \frac{\sqrt{2\pi}\,e^{-\pi ic}
      \mathfrak a(c)\mathfrak a(c/2+x)^2}
 {\mathfrak a(x)^2\mathfrak a(c/2)^6
                              \sqrt{-\mathcal K_3(c,x)}}\ne0.
 \tag{14}
\]
Its square root has positive real part. The usual
normalized fixed derivatives follow on smaller
neighborhoods. This is only the central source in
(8); no physical discarded-row or whole-run
asymptotic is inferred.

## 3. The exact lower alias and the lost \(N\)-proportional slope

Take \(x=y=x_0\) and fix \(\Re c=u\) in a compact
subinterval of \((1/2,1)\). Put \(c=u-iT\), \(T\to+\infty\),
at fixed \(N\). All moving factorial arguments in (7)
then tend into the lower half-plane. The original
exact lower factorial formula gives
\[
 \mathscr T_{3,N}(c/2+d/N,c/2-d/N;x_0,x_0)
   =C_{3,N}^-(x_0)
       e^{\pi i(N-1)c-4\pi id^2/N}(1+o(1)),
 \tag{15}
\]
uniformly in the finite set of \(d\)'s, where
\[
 C_{3,N}^-(x_0)
   =N^{-3/2}e^{-3\pi i\gamma_N}E_N(x_0)^2\ne0,\qquad
 \gamma_N=N/12-1/4+1/(12N).
 \tag{16}
\]
There are three moving numerator copies and six moving
reciprocal copies. Their lower constants give exactly
the \(N^{-3/2}e^{-3\pi i\gamma_N}\) in (16).
The full height-dependent polynomial is
\[
\begin{split}
 &2\pi iNa s+\pi iN(a+s-a^2-s^2)-\pi i(a+s)\\
 &\hspace{20mm}=\pi i(N-1)c-4\pi id^2/N.
\end{split}
 \tag{17}
\]
In particular the finite correction \(-\pi ic\)
cannot be dropped.

For the outer parity kernel
\[
             k_{\sigma,N}(c)
              =(1-e^{2\pi i\sigma}e^{-\pi iNc})^{-1},
 \tag{18}
\]
the lower alias satisfies
\(|k_{\sigma,N}(u-iT)-1|\sim e^{-\pi NT}\).
Combining this with (15) shows that every retained
row has weighted modulus
\[
 |(k_{\sigma,N}(c)-1)
       \mathscr T_{3,N}(c/2+d/N,c/2-d/N;x_0,x_0)|
          \sim |C_{3,N}^-(x_0)|e^{-\pi T}.
 \tag{19}
\]
The slope is \(\pi\), independent of \(N\).
It is not the strict positive multiple of \(N\)
available for the two-block source.

This statement also holds for the actual absolute
row majorant. With \(n_{\sigma,N}\) the number of
retained \(d\)'s in (8),
\[
 |k_{\sigma,N}(u-iT)-1|
    \sum_{|d|\le N/5}|\mathscr T_{3,N}|
       \sim n_{\sigma,N}|C_{3,N}^-(x_0)|e^{-\pi T}.
 \tag{20}
\]
The count is positive for all sufficiently large levels.
Consequently there cannot be constants
\(C,C_0,b,\lambda>0,T_0\), independent of \(N\), for which
this majorant is bounded by
\[
                    C N^b e^{N(C_0-\lambda T)}
                         \quad(T\ge T_0)
 \tag{21}
\]
at all sufficiently large levels. Choose a fixed such
\(N\) with \(\lambda N>\pi\), and then let \(T\to\infty\)
in (20). The claimed upper bound would have a strictly
faster decay rate and is impossible.

The signed sum of the rows can have additional
cancellation. Equations (19)--(21) concern the absolute
majorant used in the two-block tail proof and do not
exclude such cancellation. For every fixed level,
the bound \(e^{-\pi T}\) still removes the lower
horizontal alias.

## 4. The explicit limiting boundary rate

The lower marked primitive tends to \(i\pi/12\).
Therefore (12) gives
\[
 \lim_{T\to\infty}
       \{\Re\phi_3(u-iT,x_0)-\pi T\}
                            =-2\Re g(x_0).
 \tag{22}
\]
After restoring the outside factor \(N e^{2\pi iDx_0}\)
from (4), the corresponding boundary rate is
\[
                   E_{3,\mathrm{end}}
                      =-2\Re g(x_0)-2\pi\Im x_0.
 \tag{23}
\]
All powers of \(N\) remain prefactors in this rate statement.

The exact disk remainders also give a uniform upper
estimate with this limiting rate. There are now nine
moving factorial copies, all with depth at least
\(T/2-\Im x_0\). For \(T\ge H\) and sufficiently large
fixed \(H\), their combined logarithmic remainder is at
most
\[
                N\epsilon(H),\qquad
 \epsilon(H)\le C(1+H)e^{-\pi H+2\pi\Im x_0}
                      \longrightarrow0 .
 \tag{24}
\]
Using the original compact estimate for \(E_N(x_0)^2\),
and including the \(O(N)\) central rows, the outer
density \(N/2\), and the outside \(N\), the absolute
lower side-tail integral is bounded by
\[
       C N^{1/2}
          e^{N(E_{3,\mathrm{end}}+\epsilon(H))}e^{-\pi H}.
 \tag{25}
\]
The same estimate applies on either fixed real side
cut in the stated compact interval. Formula (25) is
obtained from the exact finite tails, not by extending
the compact-height packet (13) to infinity.

The height cutoff reduces \(\epsilon(H)\), but cannot
decrease the limiting \(N\)-rate in (23). To pay this
absolute tail at a new proposed action \(M_3\), the
mechanism requires an actual comparison with
\(E_{3,\mathrm{end}}\). Alternatively a coherent
current identity could exploit its signed cancellation.
Neither comparison is replaced by the two-block action.

## 5. Consequence for a proposed inductive Fourier criterion

This exact example separates two properties. The
central modulus inequality and Gaussian survive the
additional same-sign block, as (10)--(14) prove.
The strict \(N\)-proportional lower-tail margin used
in the two-block contour does not survive, as
(19)--(21) prove. Thus preserving only the inequality
\(S\cos\vartheta<1\), central Hessian accretivity, and
a local nonzero packet is not closure of that complete
contour criterion.

This is not a failure of the already proved ordinary
same-sign run theorem, nor a new unknown family.
The full known similarity (5), its original adapters,
and the existing ordinary two-boundary results remain
available. For genuinely mixed words or branching
clusters, any inductive Fourier argument must likewise
retain the changed boundary rates and complete current
representatives, in addition to the new critical domain.
No assertion about their general closure or the
cofinite filling theorem is made here.

