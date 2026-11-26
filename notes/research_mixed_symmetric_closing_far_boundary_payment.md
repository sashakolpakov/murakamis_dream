# Complete far samples and short endpoint currents for symmetric 343 closing

Private finite-source deduction, 9 November 2026. The full
outer \(R^4\) trace admits a strict far-angle removal and two paid
short endpoint currents at the actual symmetric geometric action.
The estimate uses the original complete matrices and all Newton
rows. It does not extend an inner packet to a new angular domain.

No mathematical numerical evaluation, saved-value arithmetic,
import, compilation, test, or frozen-source edit is used.

## 1. A sharper real-angle consequence at the actual point

Use the actual original positive symmetric point
\[
 t_g=a-iH,\quad u_g=\beta-iK,\quad
 c=\cos(t_g/2)=p+iq,\quad L=\cosh K,\quad B=\cos\beta .
\]
The [height localization](research_mixed_symmetric_closing_height_below_seven_tenths.md)
and its original unsquared identities give
\[
 0<\beta<\pi/2,\quad 17/30<K<7/10,\quad q>1/4,\qquad
 q=\sin\beta\left(L-\frac1{L-B}\right).
                                                                    \tag{1}
\]
In particular
\[
 B<L-\frac1{L-1/4}.
\]
The right side is increasing for \(L>1\). The written series
bound in the same source is \(L<157/125\), so
\[
 B<\frac{157}{125}-\frac{500}{503}
      =\frac{16471}{62875}<\frac3{10}
                         <\cos(2\pi/5).
                                                                    \tag{2}
\]
The last strict inequality follows from
\(\cos(2\pi/5)=(\sqrt5-1)/4\) and \(\sqrt5>11/5\);
the preceding one is \(164710<188625\). Therefore
\[
                              \beta>2\pi/5.                       \tag{3}
\]

Let \(S(u)=S_3(0,u)\) have the calibrated constant of the
[taller action theorem](research_mixed_symmetric_closing_strip_phase_and_tail.md),
and let
\[
 \Lambda_g=\Re\Xi(u_g),\qquad
 \Xi(u)=2S(u)+iu^2/\pi-iu .
\]
The original [closing identity](research_mixed_symmetric_343_closing_trace_and_domain.md)
identifies this action with the actual symmetric reference,
up to its already specified purely imaginary constant.
Since \(\Re S(u_g)>321/200\), (1),(3) imply
\[
 \boxed{\qquad
 \Lambda_g=2\Re S(u_g)+(2\beta/\pi-1)K
                         >321/100-7/50=307/100.
 \qquad}                                                         \tag{4}
\]
This is a bound for the same original action, not an assertion
that it already contributes to the outer finite trace.

## 2. Full real-source bounds from the original matrices

Put \(D=N-1\), \(q_N=e^{\pi i/N}\), \(\eta_N=(-1)^D\),
and retain the original Newton vector
\[
 \mathbf e(w)=(e_0(w),\ldots,e_D(w))^T,\quad
 e_j(w)=S_j^{-2}\prod_{\nu<j}(c_\nu-w),\quad
 c_\nu=2\cos((2\nu+1)\pi/N).
\]
Here \(S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N)\).
The complete crossing matrix is \(M_N\), and \(J_N\)
is exact coefficient reversal. The complete three-kernel is
\[
 Q_N^\sharp(w,x)=\mathbf e(x)^T J_NM_N^3\mathbf e(w),\qquad
 Q_N(w,u)=Q_N^\sharp(w,-2\cos u).
                                                                    \tag{5}
\]
This is the original finite polynomial, including all
coalescing-root data; there is no radical projection.

Write \(b_2=2G/\pi\) and \(c=2J(5/6)\) for the original
two- and one-crossing norm exponents. The
[full two-crossing matrix estimate](research_three_crossing_global_preparation_error.md),
Lemma 1, and the
[one-crossing norm estimate](research_three_crossing_next_step_profile.md),
Lemma 3, give
\[
 \|M_N^2\|_2\le CN^A e^{Nb_2},\qquad
 \|M_N\|_2\le CN^A e^{Nc},\qquad
 b_2<7/12,\quad c<1/3.
                                                                    \tag{6}
\]
The estimates retain the entire finite matrix. In particular
\(\|M_N^3\|_2\le CN^A e^{N(b_2+c)}\), and
\[
                              2b_2+c<3/2.                         \tag{7}
\]

The [whole real Newton theorem](research_three_crossing_real_period_newton_bound.md)
gives
\[
 \sup_{w\in[-2,2]}\|\mathbf e(w)\|_2\le CN^A e^{Nb_2},\qquad
 \|\mathbf e(-2\cos a)\|_2\le CN^A e^{Nm(a)} ,
                                                                    \tag{8}
\]
at both parities and including all \(0\le j\le D\).
Its exact real profile satisfies
\[
 m(\pi)=0,\qquad
 m'(a)=-\pi^{-1}\operatorname{arsinh}(\sin(a/2)),
              \quad0<a<\pi .
\]
Since \(\operatorname{arsinh}1<1\) (for example,
\(\sinh1>1+1/6>1\)), integration gives
\[
                      m(a)\le(\pi-|a|)/\pi
                           \quad(-\pi\le a\le\pi).                 \tag{9}
\]
The polynomial-evaluation transpose in (5) need not be
Hermitian for Cauchy--Schwarz to apply. Equations (5)--(8)
therefore prove, uniformly for real incoming \(w\),
\[
 |Q_N(w,a)|\le CN^A
      e^{N\{m(a)+2b_2+c\}},\qquad w\in[-2,2].
                                                                    \tag{10}
\]
This is a complete real-period bound, not a pointwise
packet extrapolation.

Allow two real incoming colors \(w_L,w_R\) and define
\[
 F_N(u)=Q_N(w_L,u)Q_N(w_R,u),\qquad
 G_N(u)=\sin u\,F_N(u)e^{iNu^2/\pi}.
                                                                    \tag{11}
\]
The spectral degree of \(F_N\) in \(-2\cos u\) is at most
\(2D\), and its separate degree in each incoming color is
at most \(D\). Its angular parity is exactly even.
Fix
\[
 a_F=\pi-\pi/200,\qquad
 m_N=\lfloor N/400\rfloor,\qquad
 a_N=\pi-2\pi m_N/N .
                                                                    \tag{12}
\]
For all sufficiently large \(N\),
\[
 a_F\le a_N\le\pi-\pi/400,\qquad
 e^{iNa_N}=-\eta_N .
\]
Equations (7),(9),(10) give
\[
 \sup_{\substack{w_L,w_R\in[-2,2]\\a_F\le|a|\le\pi}}
 |F_N(a)|\le CN^A e^{301N/100}.
                                                                    \tag{13}
\]
All rows remain in this bound, including every odd middle
and simple-node contribution.

## 3. Normals and the exact short verticals

As an ordinary polynomial in \(x=-2\cos a\), (13) bounds
\(F_N^\sharp(x)\) on the entire fixed interval
\[
                           I=[2\cos(\pi/200),2].
\]
Markov's inequality on this interval bounds its first
ordinary derivative at a polynomial cost. The same is
true for the first angular derivative. Differentiating
(11) adds only bounded trigonometric factors and one
power of \(N\) on the real period. Thus (13) bounds
all the original removed derivative samples \(G_N'(\tau_j)\),
where
\[
                 \tau_j=2\pi(D/2-j)/N,\qquad0\le j<N.
\]

Map \(I\) affinely onto \([-1,1]\), and use its filled
Bernstein ellipse of parameter \(e^{1/1000}\).
The exact degree \(2D\) implies
\[
 \sup_{\text{ellipse}}|F_N^\sharp|
             \le CN^A e^{N(301/100+1/500)}.
                                                                    \tag{14}
\]
The ellipse contains a fixed neighborhood of \(I\). Hence
one may choose a fixed \(h_c\in(0,1/1000]\) such that
\(-2\cos(a_N+iv)\) belongs to it for \(|v|\le h_c\),
uniformly for large \(N\).
For example its distance from \(-2\cos a_N\in I\) is
at most \(2(e^{|v|}-1)\), which tends uniformly to zero.

At either half-grid vertical the original double-pole
factor and outer crossing obey
\[
 \frac1{4\cosh^2(Nv/2)}\le e^{-N|v|},\qquad
 |e^{iN(a_N+iv)^2/\pi}|\le e^{2N|v|}.
                                                                    \tag{15}
\]
Their net cost is at most \(Nh_c\le N/1000\).
Consequently the sum of the two absolute vertical
currents, with the original \(N^2/\pi\) prefactor, has
rate at most
\[
                         301/100+3/1000=3013/1000,                \tag{16}
\]
up to a fixed polynomial. The removed physical samples
have the smaller rate in (13).

These estimates also hold on a fixed complex neighborhood
of both real incoming intervals, after a small additional
exponential cost. Indeed the removed-sample expression and
each vertical integrand are polynomials of separate degree
at most \(D\) in \(w_L,w_R\). Alternatively apply the
continuation first to the coefficient bounds in (13)--(14).
Filled incoming ellipses of parameter \(e^{1/1000}\)
cost at most \(2N/1000\) in total. On smaller fixed
neighborhoods every fixed ordinary incoming derivative
has the same exponential bound, by Cauchy's formula.

Combining this cost with (16), and spending an additional
\(2N/1000\) on every fixed polynomial factor, gives rate
at most \(3017/1000\). By (4),
\[
                  3017/1000<307/100-1/20.                        \tag{17}
\]
Thus the theorem below has one uniform reserve for the
original full normal and value data.

## 4. The paid boundary operator and literal remaining contour

Let
\[
 Z_{343,N}(w_L,w_R)
   =\mathbf e(w_L)^T(J_NM_N^3)(J_NM_N^4)
                                (J_NM_N^3)\mathbf e(w_R)
   =\phi_N[R_N^4Q_N^\sharp(w_L,\cdot)Q_N^\sharp(w_R,\cdot)] ,
                                                                    \tag{18}
\]
with the original full Hermite functional.
Set \(C_{N,4}=q_N^{D^2}\) and
\[
 W_N(u)=\frac{e^{-iNu}}{(1-\eta_Ne^{-iNu})^2}.
\]
Define its literal removed samples and paired vertical:
\[
 \mathcal R_N^{\rm far}
      =\eta_N C_{N,4}\sum_{|\tau_j|\ge a_N}G_N'(\tau_j),
\qquad
 \mathcal V_N=
 \frac{\eta_NN^2C_{N,4}}{\pi}
   \int_{-h_c}^{h_c}
      \frac{G_N(a_N+iv)}{4\cosh^2(Nv/2)}\,dv .
                                                                    \tag{19}
\]

**Theorem.** On fixed complex neighborhoods of
\(w_L,w_R\in[-2,2]\), at both parities,
\[
 |\mathcal R_N^{\rm far}|+|\mathcal V_N|
               \le C e^{N(\Lambda_g-1/20)}.                       \tag{20}
\]
The same bound holds for the sums of their absolute
samples and vertical integrands with their prefactors.
Every fixed incoming ordinary derivative obeys (20)
on smaller fixed neighborhoods.

For every piecewise smooth path \(\Gamma_N\) in the open
lower half-plane from \(-a_N-ih_c\) to \(a_N-ih_c\),
the exact remaining original source is
\[
 \boxed{\quad
 Z_{343,N}(w_L,w_R)
  =-\frac{N^2C_{N,4}}{\pi i}
       \int_{\Gamma_N}G_N(u)W_N(u)\,du
         +\mathcal V_N+\mathcal R_N^{\rm far}.
 \quad}                                                          \tag{21}
\]
Equation (21) is Corollary 3 and the contour-deformation
identity of the [complete trace theorem](research_exact_complete_trace_contour.md),
applied to the degree-\(2D\) insertion (11).
Its two vertical orientations, all higher Fourier charges,
and the complete double-root normals are unchanged.
In particular the odd central physical node is retained
inside the contour; no radical zero consumes its normal.

Equation (20) proves the asserted strict boundary payment.
It does not bound the interior of \(\Gamma_N\), or the
connections needed to bring that path to the geometric
height. The negative and intermediate far-right outer
intervals may require finite-source information outside
the current positive lower packet. No conjugation of
the fixed crossing power and no signed lower bound is
inferred from the norm estimate (10).

## Frozen source bindings

- Actual geometric point and its height below \(7/10\):
  6bf4646f6ec7b48dcbdbacfaacbe14ecb864c9d049114d3bd7c1b95fb66cc6f0.
- Taller original calibrated action and its \(321/200\) floor:
  fa1224123389462fd7e29199f1045d0892c167225b4dd6f79ea5bd967a583795.
- Exact original symmetric closing and matrix conventions:
  ef74516ae0cc9a4d965f6a528e8f582cfbca43a06e53d017201f3c30b982955a.
- Complete two-crossing matrix bound and Newton-vector bounds:
  c1e80c6efbc9ff936d889eebd1f449e85c81820a64fb046e6dfe8e1003d2d239.
- Exact complete one-crossing norm, including \(c<1/3\):
  b5343394936f80cc255cfa37ec5f410e29a453495b93bc2e1f538238199a1eac.
- All-real all-index Newton profile, monotonicity and \(b_2<7/12\):
  8759b9d7784d0c96590410969b172c95a697d86261936fd1e09201d9d12dcc2e.
- Exact arbitrary-degree Hermite trace and endpoint currents:
  a63c66e8078457fa84e8044dc876beca36126348e816de9c6997d2a2610474e8.

