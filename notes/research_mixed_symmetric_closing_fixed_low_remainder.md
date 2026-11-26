# The larger inner trace with one fixed low segment remaining

Private research deduction, 9 November 2026. The complete inner
three-crossing trace can be reduced, on the larger outgoing
rectangle, to its nonzero geometric contribution and one integral
over a fixed horizontal segment. This reduction includes the far
physical samples, their normal derivatives, the endpoint verticals,
the entire left connection, and the right far connection.

The segment still to be estimated runs from \(2\pi/3-i/10\) to
\(5\pi/6-i/10\). No estimate for that segment is asserted here.
In particular this is not a complete inner asymptotic or a theorem
about closing the tangle. No mathematical numerical evaluation or
change to a frozen source is used.

## 1. Original trace and the fixed remainder

Use the exact algebra and trace in
[the integer-power deletion theorem](research_all_integer_crossing_edge_deletions.md):
\[
 \mathcal A_N=\mathbb C[x]/(2T_N(x/2)+2),\qquad
 \phi_N(f)=(-1)^{N-1}N^2[x^{N-1}]
             \operatorname{rem}_{2T_N(x/2)+2} f .
 \tag{1}
\]
Here \(T_N\) in (1) is the Chebyshev polynomial. To avoid confusing
it with a contour endpoint, write that endpoint as \(\Theta_N\)
below. Put
\[
\begin{gathered}
 D=N-1,\quad U=\lfloor N/2\rfloor-1,\quad
 c_a=2\cos((2a+1)\pi/N),\\
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\qquad
 e_j(x)=S_j^{-2}\prod_{a<j}(c_a-x),\\
 \mathcal K_N(w,x)=\sum_{j=0}^D e_j(w)e_j(x),\qquad
 \mathcal K_N^<(w,x)=\sum_{j=0}^U e_j(w)e_j(x).
\end{gathered}                                                    \tag{2}
\]
The crossing \(R_N\) is the original element of \(\mathcal A_N\).
The full function being studied is
\[
 Q_N(u)=\phi_N\!\left[
 R_N^3\mathcal K_N(-2,x)\mathcal K_N(x,-2\cos u)\right].
 \tag{3}
\]
Both full edges occur in (3).

Let
\[
 \mathcal V_+=\{\beta-iK:0\le\beta\le\pi/2,\ 0\le K\le7/10\}.
 \tag{4}
\]
The adopted
[larger-strip theorem](research_mixed_symmetric_closing_strip_phase_and_tail.md)
fixes the original phase and its critical point:
\[
\begin{gathered}
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+3it^2/(4\pi)-it,\\
 t_*(u)=a_*(u)-iH(u),\qquad
 S(u)=\Phi(t_*(u),u),\qquad s(u)=\Re S(u)>321/200 .
\end{gathered}                                                    \tag{5}
\]
The [diagonal-taper theorem](research_mixed_symmetric_closing_diagonal_taper.md)
also proves, throughout (4),
\[
              0<a_*<\pi/2,\qquad 2/3<H<1 .                       \tag{6}
\]
All critical functions and primitive constants in this note are
those of (5).

For angular arguments abbreviate
\[
\begin{gathered}
 K_N^<(t,u)=\mathcal K_N^<(-2\cos t,-2\cos u),\\
 f_N(t,u)=K_N^<(t,0)K_N^<(t,u),\qquad
 g_N(t,u)=\sin t\,f_N(t,u)e^{3iNt^2/(4\pi)},\\
 \eta_N=(-1)^{N-1},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2},\qquad
 C_{N,3}=e^{3\pi i(N-1)^2/(4N)} .
\end{gathered}                                                    \tag{7}
\]
Define the fixed, rightward oriented segment and its exact current
by
\[
\begin{gathered}
 \gamma_{\rm low}=[\,2\pi/3-i/10,\ 5\pi/6-i/10\,],\\
 L_N(u)=-\frac{N^2C_{N,3}}{\pi i}
                  \int_{\gamma_{\rm low}}g_N(t,u)W_N(t)\,dt .
\end{gathered}                                                    \tag{8}
\]
It retains both shortened edges and the entire rational sampling
factor. The endpoints in (8) do not depend on \(u\).

**Theorem.** There is \(\epsilon>0\) such that, uniformly on (4),
for all sufficiently large integer levels of both parities,
\[
 Q_N(u)=C_{N,3}N^{-3/2}A(u)e^{NS(u)}
                     \{1+O(N^{-1})\}
          +L_N(u)+O(e^{N(s(u)-\epsilon)}),                        \tag{9}
\]
where
\[
 A(u)=\frac{i\sqrt{2\pi}}{\pi}\,
 \frac{\sin t_*(u)\,a_e(t_*(u),0)a_e(t_*(u),u)}
                      {\sqrt{-\Phi_{tt}(t_*(u),u)}}\ne0 .         \tag{10}
\]
Here \(a_e\) is the original shortened-edge coefficient in the
[taller mixed-edge theorem](research_mixed_symmetric_closing_taller_mixed_edge.md),
and the Gaussian root has its original increasing-contour
orientation. The modulus of \(A\) has a positive lower bound
on the compact rectangle (4).

## 2. Far physical samples and endpoint verticals on the larger rectangle

Write
\[
 a_F=\pi-\pi/2000,\quad
 m_N=\lfloor N/4000\rfloor,\quad
 \Theta_N=\pi-2\pi m_N/N .
 \tag{11}
\]
For all sufficiently large \(N\),
\[
 a_F\le\Theta_N\le\pi-\pi/4000<\pi,\qquad
 e^{iN\Theta_N}=-\eta_N .
 \tag{12}
\]
The original [real-period Newton bounds](research_three_crossing_real_period_newton_bound.md)
give, with one polynomial prefactor uniform in every index,
\[
\begin{split}
 \sup_{v\in\mathbb R}|e_j(-2\cos v)|&\le CN^B e^{Nb_2},\\
 |e_j(-2\cos a)|&\le CN^B e^{Nm(a)},\qquad
 m(a)\le(\pi-|a|)/\pi\quad(|a|\le\pi),\\
 b_2&<7/12 .
\end{split}                                                      \tag{13}
\]
The function \(m\) is even; its last bound follows from
\(m(\pi)=0\) and
\(m'(a)=-\pi^{-1}\operatorname{arsinh}(\sin(a/2))\).
Unlike a height estimate restricted to \(2/3\), the following
degree argument reaches the whole rectangle (4). For \(j\le U\),
expand \(e_j\) on \([-2,2]\) in Chebyshev polynomials. Each
coefficient is bounded by twice the first supremum in (13), and
\[
 |T_k(-\cos u)|\le e^{kK}.
\]
Consequently
\[
 |e_j(-2\cos u)|\le CN^{B+1}e^{N(b_2+K/2)}
                       \qquad(j\le U,\ u\in\mathcal V_+).        \tag{14}
\]
This uses the exact degree \(j\), not an asymptotic continuation.

Apply (13)--(14) separately to the two finite sums in \(f_N\).
For \(a_F\le|a|\le\pi\),
\[
 |f_N(a,u)|\le CN^B e^{NE_{\rm far}},\qquad
 E_{\rm far}=2b_2+7/20+1/1000<91/60+1/1000 .                     \tag{15}
\]
The same estimate holds if the first edge is full, since its
additional real rows satisfy (13). We use only the shortened
version in the remaining proof.

As a polynomial in \(x=-2\cos a\), \(f_N\) has degree
\(2U<N\), in particular less than \(3N/2\). The bound (15)
holds on the entire fixed interval
\[
                         I=[2\cos(\pi/2000),2].
 \tag{16}
\]
Markov's inequality on this interval bounds its first spectral
derivative at a polynomial cost. This also controls the angular
derivative, the sine in \(g_N\), and differentiation of the
crossing on the real axis. Thus every discarded far physical
sample, including its first normal, has rate at most \(E_{\rm far}\).

For clarity the endpoint-height choice can be exactly the one in
the [original boundary argument](research_mixed_next_inner_three_far_samples_and_verticals.md),
equations (27)--(31). Map \(I\) affinely onto \([-1,1]\) and use
the filled ellipse of parameter \(e^{1/6000}\). The polynomial
degree bound costs at most \(N/4000\). This ellipse contains a
fixed neighborhood of \(I\). Choose a fixed
\(0<h_c\le1/2000\) such that \(-2\cos(\Theta_N+iv)\) belongs
to it whenever \(|v|\le h_c\), uniformly in large \(N\).
The inequality
\[
 |-2\cos(\Theta_N+iv)+2\cos\Theta_N|
                         \le2(e^{|v|}-1)
\]
proves that such a choice is possible.
The exact vertical factors satisfy
\[
 \frac1{4\cosh^2(Nv/2)}\le e^{-N|v|},\qquad
 |e^{3iN(\Theta_N+iv)^2/(4\pi)}|\le e^{3N|v|/2}.
 \tag{17}
\]
Their remaining cost is at most \(N/4000\). Hence the full
endpoint-vertical integral has rate at most \(E_{\rm far}+1/2000\),
with its original prefactor \(N^2\).
There is a fixed reserve:
\[
 \frac{321}{200}
   -\left(\frac{91}{60}+\frac3{2000}\right)-\frac1{20}
                              =\frac{221}{6000}>0 .             \tag{18}
\]
Polynomial factors are absorbed into this reserve.

The exact derivative-sampling and contour identities in the
boundary argument are algebraic identities for this same
polynomial \(f_N\); their dependence on \(u\) is entirely through
its coefficients. Applying the bounds just proved therefore
gives, for any lower-half-plane path \(\Gamma_N\) from
\(-\Theta_N-ih_c\) to \(\Theta_N-ih_c\),
\[
 Q_{3,N}^{<<}(-2,u)
   =-\frac{N^2C_{N,3}}{\pi i}
         \int_{\Gamma_N}g_N(t,u)W_N(t)\,dt
          +O(e^{N(s(u)-1/20)}).                                 \tag{19}
\]
The trace on the left is the full trace (1), with both edges
shortened. Its odd simple node is retained by the exact identity.
Only the explicitly estimated far samples have been removed.

## 3. The whole left connection

Use the original path
\[
 -\Theta_N-ih_c\longrightarrow-\Theta_N-iH(u)
                         \longrightarrow-\pi/2-iH(u).           \tag{20}
\]
The [slit-plane source theorem](research_mixed_next_first_short_edge_slit_plane_bound.md),
equations (18), (23), and (24), gives, for every fixed \(\tau>0\),
\[
 |f_N(-a-ih,u)|
 \le CN^B\exp N\{2\Re\psi(a-ih,0)+K/2+2\tau\}                   \tag{21}
\]
on \(\pi/2\le a\le\pi-\pi/4000,\ 0\le h\le1\).
The second factor follows from its entire real outside period
and its exact degree \(U\). Evenness and real coefficients
give the negative first-angle version in (21).

At height \(H=H(u)\), the crossing and full sampling denominator
give the additional rate \(-3aH/(2\pi)-H\). The resulting
rate
\[
 E(a,u)=2\Re\psi(a-iH,0)+K/2-H-3aH/(2\pi)                       \tag{22}
\]
decreases with \(a\), because
\(\psi_t(t,0)=-\pi^{-1}\operatorname{arsinh}\tan(t/2)\)
has negative real part in this first-angle region.

We give the comparison at \(a=\pi/2\), including the change of
outgoing height. Put \(t_R=\pi/2-iH\). Here
\(|\cos(t_R/2)|<1\) and \(0<\arg\cos(t_R/2)<H/2\).
Along a real outgoing segment, the real part of its principal
return is bounded by
\(\operatorname{arsinh}(\tan(v/2))\). Since
\(\psi(0,0)<7/6\) and
\(\psi(0,\pi/2)>239/250\), integration gives
\[
 \Re\psi(t_R,0)-\Re\psi(t_R,\beta)<79/375 .                       \tag{23}
\]
On the subsequent segment \(\beta-ik\), its return has imaginary
part less than \(H/2\): if that imaginary part is positive, it
is less than the argument of its hyperbolic sine, which in turn
is at most \(\arg\cos(t_R/2)\). If it is nonpositive the desired
upper bound is automatic. The principal branch throughout this
larger segment is the one proved by the taller mixed-edge theorem.
It follows that
\[
 \Re\psi(t_R,0)-\Re\psi(t_R,u)<79/375+HK/(2\pi).                  \tag{24}
\]
The central horizontal concavity gives
\[
 s(u)\ge\Re\psi(t_R,0)+\Re\psi(t_R,u)-H/4 .
 \tag{25}
\]
Subtract (22) at \(a=\pi/2\). Using \(2/3<H<1\),
\(K\le7/10\), and \(\pi>3\), we obtain
\[
 s(u)-E(\pi/2,u)
 >3H/2-K/2-79/375-HK/(2\pi)
 >1-7/20-79/375-7/60=121/375 .                                  \tag{26}
\]
For example, take \(\tau=1/10000\) in (21). The reserve in
(26) after a gap \(1/4\) and these two tolerances is positive.
It absorbs all polynomial factors and the original \(N^2/\pi\).
The horizontal part of (20) consequently has gap \(1/4\).

On its entire vertical part the half-grid identity gives
\[
 |W_N(-\Theta_N-ih)|
       =\frac{e^{-Nh}}{(1+e^{-Nh})^2}\le e^{-Nh}.
\]
The exact return satisfies
\(\partial_h\Re\psi(a-ih,0)<1/2\). Thus the vertical rate in
(22), with \(H\) replaced by \(h\), decreases with \(h\).
Its maximum is bounded by \(2\psi(\Theta_N,0)+K/2\).
The original integrated return gives
\[
 \psi(\pi-\delta,0)
  <\frac{\delta}{\pi}\left(1+\log\frac4\delta\right),\qquad
 \psi(\Theta_N,0)<1/200 .                                       \tag{27}
\]
For the last bound use \(\delta=\pi/2000\) and
\(\log(8000/\pi)<9\), as proved in the original left-connection
note. Consequently this whole vertical has rate less than
\(1/100+7/20=9/25\), before the arbitrary tolerances.
The floor \(s>321/200\) pays it with more than the claimed
gap \(1/4\). This proves the complete left-path bound.

## 4. The right far connection

Keep the fixed rightward-then-upward path
\[
 5\pi/6-i/10\longrightarrow\Theta_N-i/10
                           \longrightarrow\Theta_N-ih_c .
 \tag{28}
\]
The calibrated real first-edge estimate in
[the original far-region proof](research_mixed_next_inner_three_right_far_region.md)
is
\[
 \psi(a,0)\le\psi(5\pi/6,0)<13/24\qquad(5\pi/6\le a<\pi).
 \tag{29}
\]
It follows directly by writing
\(\psi(5\pi/6,0)=-4\int_0^{1/24}\log\tan(\pi x)\,dx\)
and using \(\tan(\pi x)>\pi x\), \(\pi>3\), and \(\log8<9/4\).
Integrating the same height derivative as above gives
\[
                 2\Re\psi(a-ih,0)<13/12+h .
 \tag{30}
\]
Use the slit theorem for both complete shortened factors.
At \(0<h\le1/10\), their product, crossing, and sampling
kernel have rate at most
\[
\begin{split}
 2\Re\psi(a-ih,0)+K/2-h+3ah/(2\pi)+2\tau
       &<13/12+7/20+3/20+2\tau\\
       &=19/12+2\tau .
\end{split}                                                      \tag{31}
\]
The kernel bound is uniform for \(h\ge h_c\). On the endpoint
column it also holds at \(h=0\), by the exact half-grid formula.
With \(\tau=1/10000\), the reserve is
\[
 \frac{321}{200}-\frac{19}{12}-\frac1{5000}-\frac1{50}
                         =\frac{11}{7500}>0 .                   \tag{32}
\]
Thus the absolute current on (28), including \(N^2/\pi\),
is \(O(e^{N(s-1/50)})\). No estimate restricted to outgoing
height \(1/2\) has been used for the larger rectangle.

## 5. Assembly and the remaining analytic question

Choose the path in (19) as the following concatenation:

1. The left connection (20).
2. The full central horizontal from \(-\pi/2-iH\) to
   \(\pi/2-iH\).
3. The diagonal and vertical path of the diagonal-taper theorem,
   ending at \(2\pi/3-i/10\).
4. The fixed segment \(\gamma_{\rm low}\) in (8).
5. The right far connection (28).

All these paths lie strictly below the sampling poles. The
finite integrand is holomorphic there, so the replacement
preserves the exact current without adding residues.

The taller mixed-edge theorem bounds every portion of the
central horizontal separated from \(t_*(u)\) below \(s(u)\),
including the interval across the imaginary axis. In a fixed
neighborhood of the critical point, apply its full relative
packet to each shortened edge, with outgoing angles \(0\)
and \(u\), respectively. The product has coefficient
\(N^{-3}a_e(t,0)a_e(t,u)\), and
\[
 W_N(t)=e^{-iNt}\{1+O(e^{-cN})\}
\]
there, by the uniform positive depth in (6). The local
Gaussian integral, with the original prefactor, therefore
has exactly (10) and the factor \(C_{N,3}N^{-3/2}\).
Both edge coefficients, the sine, and the Hessian are nonzero;
compactness gives their uniform margins. This proves the
central asymptotic with relative error \(O(N^{-1})\).

The diagonal-taper theorem supplies a uniform positive
gap for part 3. Sections 2--4 above supply the far sample,
endpoint, left, and right far gaps. Taking their minimum
with the central remote gap yields a positive \(\epsilon\).
Finally the integer-power deletion theorem, equation (23),
restores both full edges in (3) at an error
\(O(e^{N(s-1/25)})\). Include \(1/25\) in that minimum.
This proves (9).

An estimate
\[
 |L_N(u)|\le CN^B e^{N(s(u)-\delta)},\qquad \delta>0,
 \tag{33}
\]
on the required outgoing domain would now give a complete
inner asymptotic there. Equation (33) is not proved by this
note. In addition, using such an asymptotic in the outer
closing trace requires the actual closing critical point
to lie in its domain and requires bounds for that outer
trace's remaining contributions. These are separate from
the finite-exception theorem's requirement of stability
under arbitrary fixed short partial fillings.

## Source versions

- Original larger cubic/action:
  fa1224123389462fd7e29199f1045d0892c167225b4dd6f79ea5bd967a583795.
- Complete taller mixed-edge packet and signed central bound:
  01630dd45f907e7d116fc8d51fed0ef00e13176f379b5ce1ab0186403cd1a94c.
- Complete diagonal and vertical attached payment:
  7ba93b34b12765ebdfec7853ffc1e7e77bc370e07770c9088f59e538785af908.
- Exact both-edge trace deletion:
  f7abba0175c558ee9ca7f94799f9cd4d58adc249fea3f6b8c425e55a8136da66.
- All original real Newton rows:
  8759b9d7784d0c96590410969b172c95a697d86261936fd1e09201d9d12dcc2e.
- Exact far derivative sampling and endpoint contour identity:
  15a38af35c84cacc940f11a7c22675748d5f9da7fc19424573116dcdbf77c685.
- Complete shortened first edge and full outside-period bound:
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
- Original left connection and its calibrated endpoint:
  0981672faffc8d4cb94848a59ce01eeeb9627110e05fed16a2664ba8c27f930f.
- Original right far connection and calibrated real integral:
  d610fce6cd5f9e4786606796bff247b88e48e6021f85b3542178a4d3dc93ba9e.
- Complete-edge real anchor:
  1ac5e324eeb4f11425b6937332e08a682c802ce3d1fb3b6646cf7ecffed38ac3.
- Original one-current normalization:
  2c5be7138aed7dabbb06f04010c602ee095fa8ceb62ec213e75e4d628aa95421.
