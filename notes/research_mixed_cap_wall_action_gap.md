# The wrapped cap rows lie below the cap's critical action

Research deduction, 8 November 2026. For the real incoming arc,
the bound for all wrapped private cap rows is strictly below
the original cap critical action. The comparison follows from
the endpoint action derivative and horizontal concavity. It
does not require an evaluation of that action.

This pays the complete wrapped physical sector and a small
real collar before its wall. The left private contour and the
remaining outer-cap currents still require their own estimates.
No numerical evaluation is used.

## 1. Original phases and the actual critical path

Retain the endpoint phase and cap phase at complete ordinary color:
\[
\begin{split}
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 S(e)&=F(e,u_c(e)),\qquad F_u(e,u_c)=0,\\
 \Psi(e,a)&=S(e)+J(e+a)-J(a)-i\pi ea,
                       \qquad \frac12\le a\le\frac7{10}.
\end{split}                                                       \tag{1}
\]
Every logarithm, stationary branch and primitive constant is
the original one. Write
\[
 e_*(a)=E_*(a)+ih_*(a),\qquad
 \Psi_e(e_*(a),a)=0,\qquad
 M_{\rm cap}(a)=\Re\Psi(e_*(a),a),\qquad v=1-a.
                                                               \tag{2}
\]
The [actual cap-path theorem](research_mixed_endpoint_actual_cap_path_bridge.md)
and the original branch theorem prove
\[
 \frac6{25}<E_*<\frac9{20},\qquad
 -\frac3{50}<h_*<0,\qquad E_*<v,\qquad
                      \frac3{10}\le v\le\frac12.
                                                               \tag{3}
\]
The critical path is continuous on its compact incoming arc.
In particular \(d_{\min}:=\min_a(v-E_*)>0\).

The real endpoint profile is
\[
             \lambda(E)=\Re S(E),\qquad h(E)=\lambda(E)+J(E).
                                                               \tag{4}
\]
The letter \(h\) in (4) denotes a real profile; \(h_*(a)\)
in (2) is the cap critical height.
The [wrapped-row theorem](research_mixed_cap_wrapped_row_transport.md)
already bounds the complete positive wrapped row sum by
the exponential rate \(h(v)\), with all original factors
retained. We prove its missing comparison with \(M_{\rm cap}\).

## 2. Two derivative inequalities for the endpoint action

The selected endpoint action satisfies the exact identities
\[
\begin{split}
 S'(e)&=-J'(e-u_c(e))+i\pi u_c(e),\\
 -S''(e)&=\pi\cot\pi e+
             \frac{2\pi}{\sin\pi e\sqrt{\,2-e^{-2\pi ie}\,}} .
\end{split}                                                       \tag{5}
\]
These identities, including the square-root branch, are proved
in the original endpoint and cap curvature notes.

They extend to the compact rectangle
\[
             \frac6{25}\le\Re e\le\frac12,\qquad
                         -\frac3{50}\le\Im e\le0.
                                                               \tag{6}
\]
For clarity, the upper real boundary is not a new singular
endpoint branch. Put \(p=e^{2\pi ie}\) and
\(\omega=e^{2\pi iu_c}\). On \(\Re e<1/2\), the
[bridge phase theorem](research_mixed_endpoint_bridge_phase_floor.md)
selects the upper root of
\[
                  (p-5)\omega^2+2(p+1)\omega+p-1=0.
                                                               \tag{7}
\]
At \(\Re e=1/2\), \(p=-R\) with \(R\ge1\), and that root is
\[
                 \omega=\frac{1-R+2i\sqrt{2R+1}}{R+5}.
                                                               \tag{8}
\]
It is simple and remains strictly upper. At \(R=1\),
\(\Re u_c=\Re(e-u_c)=1/4\); for \(R>1\),
\(1/4<\Re u_c<1/2\) and \(0<\Re(e-u_c)<1/4\).
All original primitive
arguments remain regular. The discriminant \(16(2p-1)\)
never vanishes on (6), and the indicated square root in
(5) has positive real part. Thus the selected branch,
its zero lift and (5) extend through this boundary,
by continuity and the implicit-function theorem.

**Lemma 1.** On (6), \(-\Re S''(e)>0\). Moreover
\[
               \Im S'(E+i\sigma)>\frac{\pi}{4}
       \quad\left(\frac14\le E\le\frac12,\
                              -\frac3{50}\le\sigma\le0\right).
                                                               \tag{9}
\]

*Proof.* For the first assertion, \(\Re\cot\pi e\ge0\)
on (6). Also
\[
 -\frac3{10}<\arg\sin\pi e\le0,\qquad
        0\le\arg\sqrt{2-e^{-2\pi ie}}<\frac{\pi}{4}.
                                                               \tag{10}
\]
Indeed \(\cot(\pi\Re e)<3/2\), since
\(\Re e\ge6/25>1/5\) and \(\tan(\pi/5)>2/3\).
The sine argument has tangent
\(\cot(\pi\Re e)\tanh(\pi\Im e)\), whose modulus is
less than \(9\pi/100<3/10\).
For the other argument, \(e^{-2\pi ie}\) has modulus
at most one and nonpositive imaginary part; hence
\(\Re(2-e^{-2\pi ie})\ge1\) and its imaginary part is
nonnegative. Thus the reciprocal product in (5) has
strictly positive real part. This proves \(-\Re S''>0\).

We fix a useful derivative value at \(E=1/4\) algebraically.
Here \(p=i\). Define
\[
                             q=\frac{\omega}{p-\omega}.
\]
Substitution in (7) gives
\[
                          -2iq^2+4q+1=0.
                                                               \tag{11}
\]
Let \(d=\sqrt{1+i/2}\) be the root with positive real
and imaginary parts. The solution
\[
                            q=-i(1+d)
                                                               \tag{12}
\]
has positive real part and negative imaginary part.
Its corresponding \(\omega=iq/(1+q)\) is upper, since
\[
       \Im\omega=\frac{\Re q+|q|^2}{|1+q|^2}>0.
                                                               \tag{13}
\]
The unique upper endpoint root therefore selects (12).
The first identity in (5) gives, with the original
square roots,
\[
                         e^{S'(1/4)}
                            =i\sqrt p\,q=e^{3\pi i/4}q.
                                                               \tag{14}
\]
Its argument lies in \((\pi/4,3\pi/4)\).
There is no logarithmic ambiguity: the bridge phase
theorem gives \(\Im u_c>0\) at real \(e=1/4\) and
\(0<\Re u_c<1/4\). Consequently \(e-u_c\) has negative
height and real part in \((0,1/4)\), so the original
formula in (5) has
\[
                         0<\Im S'(1/4)<3\pi/4.
                                                               \tag{15}
\]
Equations (14)--(15) imply \(\Im S'(1/4)>\pi/4\).

On the real interval \(1/4\le E\le1/2\), (5) gives
\(\Im S''(E)\ge0\). The cotangent is real, while
the inverse square root has nonpositive imaginary
part and is multiplied by a negative real factor
in \(S''\). Thus
\(\Im S'(E)\ge\Im S'(1/4)>\pi/4\).
Finally
\[
             \partial_\sigma\Im S'(E+i\sigma)
                                      =\Re S''(E+i\sigma)<0.
                                                               \tag{16}
\]
Moving down from the real axis increases this imaginary
derivative. This proves (9). \(\square\)

## 3. Comparing the real wall with the actual cap saddle

The cap phase has the continuous left wall value
\[
                  \Re\Psi(v,a)=\lambda(v)+J(v)=h(v),
                                                               \tag{17}
\]
since \(a+v=1\), \(J(1)=0\), \(J(a)=-J(v)\), and the
remaining linear term in (1) is imaginary at real \(a,v\).

For \(-3/50\le\sigma<0\), the original left boundary
value of \(J'(1+i\sigma)\) has imaginary part \(\pi/2\).
Indeed \(\sin\pi(1+i\sigma)=-i\sinh(\pi\sigma)\) is
positive imaginary. Lemma 1 therefore implies
\[
\begin{split}
 \Im\Psi_e(v+i\sigma,a)
     &=\Im S'(v+i\sigma)+\frac{\pi}{2}-\pi a\\
     &=\Im S'(v+i\sigma)+\pi(v-1/2)
       >\pi(v-1/4)\ge\frac{\pi}{20}.
\end{split}                                                       \tag{18}
\]
The primitive is continuous at \(\sigma=0\), despite
the logarithmic derivative there. Integrating
\(\partial_\sigma\Re\Psi=-\Im\Psi_e\) gives
\[
       \Re\Psi(v+ih_*,a)>
                     h(v)+\frac{\pi}{20}|h_*|.
                                                               \tag{19}
\]

On the horizontal segment from \(e_*=E_*+ih_*\) to
\(v+ih_*\), the incoming real part \(a+\Re e\)
lies between \(1/2\) and one. Hence
\[
 -\Re\Psi_{ee}
        =-\Re S''(e)-\pi\Re\cot\pi(a+e)
                            \ge-\Re S''(e)>0.
                                                               \tag{20}
\]
Let \(\kappa>0\) be the minimum of \(-\Re S''\)
on (6). This minimum is positive by Lemma 1 and
compactness. Twice integrating (20) from the actual
stationary point, where \(\Psi_e(e_*,a)=0\), gives
\[
 M_{\rm cap}(a)-\Re\Psi(v+ih_*,a)
                  \ge\frac{\kappa}{2}(v-E_*)^2.
                                                               \tag{21}
\]
The right endpoint has \(h_*<0\), so it is not a
factorial zero or a primitive singularity.

Combining (19)--(21) proves the uniform strict comparison
\[
 \boxed{\quad
 M_{\rm cap}(a)-h(1-a)>
       \frac{\kappa d_{\min}^2}{2}
                       +\frac{\pi}{20}|h_*(a)|>0,
                       \qquad \frac12\le a\le\frac7{10}.
 \quad}                                                         \tag{22}
\]
The constants are defined by proved strict inequalities
on compact sets. No action value or minimum is evaluated.

## 4. The complete wrapped finite sector

The literal cap is
\[
 U_{0,N}(w,X)=\sum_{j=0}^{N-1}
          H_N(w,r^{-j})\frac{p_j(X)}{P_j},
 \qquad r=e^{-2\pi i/N},\quad X=e^{-2\pi ia}.
                                                               \tag{23}
\]
Each \(H_N\) in (23) is the complete original endpoint
polynomial. The wrapped-row transport theorem proves,
for every prescribed tolerance \(\tau>0\),
\[
 \sum_{j/N\ge1-a}
   \left|H_N(w,r^{-j})p_j(X)/P_j\right|
       \le C_\tau N^{B_\tau}e^{N\{h(1-a)+\tau\}},
                           \qquad -2\le w\le2.
                                                               \tag{24}
\]
It includes the true physical endpoint, all numerator
zeros and both level parities.
Choose the tolerance inside the fixed gap (22).
There are therefore constants \(C,B,\delta>0\) such that
\[
 \sum_{j/N\ge1-a}
   \left|H_N(w,r^{-j})p_j(X)/P_j\right|
            \le C N^B e^{N\{M_{\rm cap}(a)-\delta\}}
                                                               \tag{25}
\]
uniformly on the real incoming and ordinary-color
ranges just stated.

The same physical row profile is continuous at \(e=1-a\):
its original zero-safe integrated logarithm is finite
there and equals (17). Compactness and (22) consequently
also pay a fixed sufficiently small real collar before
the wall. Fixed row subsets have the local complex and
fixed-derivative bounds supplied by the wrapped-row theorem,
after allocating a smaller part of the gap. No moving
integer cutoff is differentiated.

Equation (25) completes one required outer-cap estimate.
It does not supply the endpoint coefficient on an entire
leftward private contour, estimate all outer aliases,
or identify the full cap with its local Gaussian.
Those source obligations and the subsequent product
comparison remain separate.
