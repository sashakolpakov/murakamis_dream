# A test of half-plane positivity for the original terminal periods

Research note, 3 November 2026.

The complete terminal \(H_2=T(R^2)\) has a period that becomes a
Pick function after subtracting its linear imaginary term. This
suggests a possible way of organizing short turns. The same property,
however, fails for all sufficiently large terminal powers, even after
an arbitrary linear imaginary correction. The obstruction occurs in
the cubic Taylor coefficient of the actual marked period.

These are statements about the geometric phase germs already
identified by the terminal source theorems. They do not assert a
global asymptotic expansion of the quantum source on the domains
used for analytic continuation below.

## 1. The two-crossing test

A Pick function here means a holomorphic function on the upper
half-plane with nonnegative imaginary part. Put
\[
 f(u)=\log\tan\left(\frac\pi4+\frac u4\right),
 \qquad f(0)=0,
 \tag{1}
\]
initially on the complete branch. On \(|\Re u|<\pi\),
\[
 f(u)=\operatorname{arsinh}\tan(u/2)
     =\operatorname{artanh}\sin(u/2),\qquad
 f'(u)=\frac12\sec(u/2).
 \tag{2}
\]
The equalities follow by differentiating and evaluating at zero.
All the displayed branches are holomorphic on this vertical strip.

The phase in
[the original two-crossing theorem](research_two_crossing_terminal_filling.md)
satisfies
\[
 W_2'(u)=-\frac{f(u)}{2\pi}-\frac{iu}{4\pi}.
 \tag{3}
\]
Its pure boundary period is therefore
\[
                         U_2(u)=-2\pi W_2'(u)=f(u)+iu/2.
 \tag{4}
\]
Any separately specified outside carrier changes this period only
by its prescribed linear imaginary term.

**Proposition 1.** The function \(f\) extends to a Pick function
on the entire upper half-plane, with \(0<\Im f<\pi\). The full
period \(U_2\) is not a Pick function. Nevertheless,
\[
                  \Re U_2'(u)=\tfrac12\Re\sec(u/2)>0
                    \qquad (|\Re u|<\pi).
 \tag{5}
\]

**Proof.** For \(z=x+iy\), \(y>0\),
\[
 \Im\tan z=\frac{\sinh(2y)}{\cos(2x)+\cosh(2y)}>0.
 \tag{6}
\]
Thus \(\tan(\pi/4+u/4)\) lies in the upper half-plane whenever
\(\Im u>0\). Its principal logarithm is holomorphic and has
imaginary part between \(0\) and \(\pi\), proving the first claim.
Equation (6) is also the standard real/imaginary-part tangent
identity in [DLMF §4.21(iv)](https://dlmf.nist.gov/4.21.iv).

For \(0<a<\pi\), let \(u=-a+i\varepsilon\) and let
\(\varepsilon\downarrow0\). The boundary value \(f(-a)\) is
real, whereas \(\Im(iu/2)=-a/2\). Hence \(U_2\) takes values
with negative imaginary part in the upper half-plane.

Finally \(\Re\cos(u/2)>0\) on the indicated vertical strip,
so its reciprocal also has positive real part. Equations
(2),(4) give (5). For distinct \(z,w\) in this convex strip,
integration along the segment gives
\[
             \Re\frac{U_2(z)-U_2(w)}{z-w}>0.
\]
Thus \(U_2\) is injective there, and its real part strictly
increases along each horizontal line. \(\square\)

The conjugate terminal has \(U_{-2}=f-iu/2\). It fails the Pick
condition near a positive real \(u\), for the same reason.
Thus the linear term must already be recorded for either sign.

## 2. A necessary condition for an odd Pick germ

**Lemma 2.** Let \(g\) be holomorphic near zero, odd there, and
suppose it extends as a Pick function on the upper half-plane.
Then \(g\) is real on a real neighborhood of zero. In particular
every Taylor coefficient of \(g\) at zero is real.

**Proof.** Continuity from above gives \(\Im g(x)\ge0\) for
sufficiently small real \(x\). Oddness gives
\(\Im g(-x)=-\Im g(x)\); both numbers are nonnegative, hence
both vanish. Derivatives of a holomorphic function real on a real
interval have real Taylor coefficients. \(\square\)

The same argument rules out an upper-half-plane map on any
two-sided upper half-disk around zero. This is a local obstruction,
not an assumption about the behavior at infinity.

## 3. The cubic coefficient for an arbitrary terminal power

For a fixed nonzero power \(p\) in the proved terminal range, let
\(t_p(u)\) be its selected critical point. On the complete branch,
\[
 \psi_t(t_p(u),u)+\frac{ip}{2\pi}t_p(u)=i,\qquad
 W_p(u)=\psi(t_p(u),u)+\frac{ip}{4\pi}t_p(u)^2-it_p(u).
 \tag{7}
\]
A constant unit-phase normalization in \(W_p\) has no effect below.
The original pure period is
\[
 U_p(u)=-2\pi W_p'(u)
       =2\operatorname{arsinh}
                    \bigl(\tan(u/2)\cos(t_p(u)/2)\bigr).
 \tag{8}
\]
Separate evenness implies that \(t_p\) is even and \(U_p\) is odd.
Write
\[
 t_0=t_p(0),\qquad k=\cos(t_0/2),\qquad s_0=\sin(t_0/2).
 \tag{9}
\]
The symbol \(s_0\) is distinct from the inverse-power parameter
used in the next section.

**Proposition 3.** At the original complete boundary,
\[
 U_p'(0)=k,\qquad
 \boxed{\displaystyle
 U_p'''(0)=\frac{k(2-k^2)}4
              -\frac{3(1-k^2)k}{4(1-ipk)}.}
 \tag{10}
\]

**Proof.** The edge derivative gives
\[
 \psi_{tt}(t_0,0)=-\frac1{2\pi k},\qquad
 \psi_{tuu}(t_0,0)=\frac{s_0}{4\pi}.
 \tag{11}
\]
Twice differentiating (7), and using \(t_p'(0)=0\), yields
\[
                    t_p''(0)=\frac{s_0k}{2(1-ipk)}.
 \tag{12}
\]
The denominator is nonzero on the selected nondegenerate branch.
If \(q(u)=\tan(u/2)\cos(t_p(u)/2)\), then
\[
 q'(0)=k/2,\qquad
 q'''(0)=k/4-3s_0t_p''(0)/4.
 \tag{13}
\]
Since \((\operatorname{arsinh}q)'''(0)=q'''(0)-q'(0)^3\),
substituting (12) into \(U_p'''=2q'''-2q'^3\) gives (10).
The identity \(s_0^2=1-k^2\) completes the simplification. \(\square\)

For \(p=2\), \(k=(1+i)/2\). Formula (10) gives
\(U_2'''(0)=1/8\), in agreement with (2),(4).

## 4. Long terminals already obstruct Pick plus a quadratic phase

Set \(s=1/p\). The analytic rescaling in
[the uniform terminal-family proof](research_uniform_terminal_family_and_star_fillings.md)
also follows directly at \(u=0\) from
\[
                    t(s)=2\pi s-2is f(t(s)).
 \tag{14}
\]
The derivative with respect to \(t\) at \(s=t=0\) is one, so the
holomorphic implicit-function theorem gives an analytic solution
near \(s=0\). Its Taylor expansion is
\[
 \begin{split}
 t(s)&=2\pi s-2\pi i s^2+O(s^3),\\
 k(s)&=1-\frac{\pi^2}{2}s^2+i\pi^2s^3+O(s^4).
 \end{split}
 \tag{15}
\]
The first equation follows by \(f(t)=t/2+O(t^3)\); the second
follows by expanding the cosine. Consequently
\[
 \frac1{1-ik(s)/s}=\frac{is}{k(s)}+O(s^2),
 \qquad
 U_{1/s}'''(0)
       =\frac14+\frac{\pi^2}{8}s^2-i\pi^2s^3+O(s^4).
 \tag{16}
\]
These are convergent-germ Taylor estimates. In particular
\[
                  \Im U_p'''(0)=-\frac{\pi^2}{p^3}
                                      +O(p^{-4})
 \tag{17}
\]
for positive real \(p\) tending to infinity along the selected
branch. Its imaginary part is strictly negative for every
sufficiently large positive integer \(p\).

**Corollary 4.** For all sufficiently large positive integers
\(p\), no real number \(\gamma\) makes
\[
                              U_p(u)-i\gamma u
 \tag{18}
\]
a Pick germ near zero. The same assertion holds for all
sufficiently large negative integers, by conjugation.

**Proof.** The function (18) is odd. Its third derivative is
unchanged by the linear correction and has nonzero imaginary
part by (17). This contradicts Lemma 2. \(\square\)

Thus a proposed class of original period maps consisting of
Pick functions plus explicit linear imaginary filling terms
does not contain even all the already-proved long terminal
pieces. Adding the known quadratic boundary phase to the action
cannot fix this obstruction.

## 5. A single real nonlinear boundary coordinate does not repair the class

There is a stronger obstruction to one fixed scalar change of
coordinates. Let \(u=\chi(q)\) be any real odd holomorphic germ,
independent of \(p\), with \(\chi'(0)=a>0\). The canonical
transformed response, preserving the action differential, is
\[
 \widetilde U_p(q)=U_p(\chi(q))\chi'(q)
                  =-2\pi\frac{d}{dq}W_p(\chi(q)).
 \tag{19}
\]

**Proposition 5.** No such fixed \(\chi\) makes
\(\widetilde U_p(q)-i\gamma_pq\) a Pick germ for every sufficiently
large positive integer \(p\), even if the real correction
\(\gamma_p\) is allowed to depend on \(p\).

**Proof.** Write \(s=1/p\), \(c=\cos(u/2)\), and
\(x=\sin^2(u/2)=1-c^2\). The full terminal stationary equation
on this boundary is
\[
 t=2\pi s-2is\operatorname{arsinh}\bigl(c\tan(t/2)\bigr).
 \tag{20}
\]
It has a jointly holomorphic solution for \(s,u\) near zero,
by the implicit-function theorem. The Taylor expansion
\[
 2\operatorname{arsinh}\bigl(c\tan(t/2)\bigr)
          =ct+\frac{2c-c^3}{24}t^3+O(t^5)
 \tag{21}
\]
determines its coefficients successively:
\[
 \begin{split}
 t={}&2\pi s-2\pi ic\,s^2-2\pi c^2s^3\\
 &+i\left(2\pi c^3+\frac{\pi^3c^3}{3}
                         -\frac{2\pi^3c}{3}\right)s^4\\
 &+\left(2\pi c^4+\frac{4\pi^3c^4}{3}
                         -\frac{8\pi^3c^2}{3}\right)s^5
   +O(s^6).
 \end{split}
 \tag{22}
\]
Substitution in (20) with (21) checks each coefficient; the
omitted \(t^5\) term first affects \(s^6\). The envelope identity
for the action is
\[
 \frac{\partial W_{1/s}(u)}{\partial s}
                =-\frac{i\,t(s,u)^2}{4\pi s^2}.
 \tag{23}
\]
The right side is holomorphic at \(s=0\), and
\(W_{1/s}(u)\to\psi(0,u)\) there. Squaring (22), integrating
(23), and subtracting the value at \(u=0\) gives, for real \(s,u\),
\[
 \boxed{\displaystyle
 \Im\bigl[W_{1/s}(u)-W_{1/s}(0)\bigr]
   =-\pi x s^3+
        \left[2\pi x-\left(\pi+\frac{\pi^3}{3}\right)x^2\right]s^5
        +O(s^7).}
 \tag{24}
\]
The remainder and its fixed \(u\)-derivatives are uniform near
zero. The improvement to \(O(s^7)\) uses the exact real-parameter
symmetry \(W_{-1/s}(u)=\overline{W_{1/s}(u)}\); the imaginary
part has only odd powers of \(s\). A constant choice of marked
action does not change the normalized difference in (24).

If the response in the proposition were Pick, Lemma 2 would
make its Taylor coefficients real. Integrating in \(q\) shows
that the imaginary part of the normalized action
\(W_p(\chi(q))-W_p(0)\) must be a quadratic function of \(q\).
Its coefficients of \(q^4,q^6,\ldots\) vanish for all sufficiently
large integers \(p\). Those coefficients are real-analytic
functions of \(s\) near zero. Their zeros at \(s=1/p\) accumulate
at zero, so they vanish identically. Consequently each
coefficient of \(s\) in (24) must itself be quadratic in \(q\).

The \(s^3\) coefficient forces
\[
               \sin^2(\chi(q)/2)=\frac{a^2q^2}{4},
 \qquad \chi(q)=2\arcsin(aq/2)
 \tag{25}
\]
on the selected germ. The \(s^5\) coefficient then contains
\[
              -\left(\pi+\frac{\pi^3}{3}\right)
                         \frac{a^4q^4}{16},
 \tag{26}
\]
which is nonzero. This contradiction proves the proposition.
\(\square\)

The same obstruction holds if one merely reparametrizes the
input and asks for \(U_p(\chi(q))-i\gamma_pq\) to be Pick,
without the factor \(\chi'\) in (19). Differentiating (24) gives
\[
 \Im U_{1/s}(u)=\pi^2\sin u\,s^3+
 \left[-\pi^2+\frac{\pi^4}{3}
       -\left(\pi^2+\frac{\pi^4}{3}\right)\cos u\right]
          \sin u\,s^5+O(s^7).
 \tag{27}
\]
The first coefficient would force \(\sin\chi(q)=a q\). The next
then has the nonzero cubic coefficient
\((\pi^2+\pi^4/3)a^3/2\). Lemma 2 again gives a contradiction.

## 6. What remains possible

These tests exclude a fixed real scalar reparametrization and a
linear imaginary correction as a common Pick description of
the already-proved terminal family. They do not exclude
power-dependent charts, transformations mixing both primitive
periods, a matrix-valued positivity condition, or the
positive-domain monotonicity proved in
[the original edge geometry](research_positive_edge_global_monotonicity.md).
Those alternatives must keep the primitive marking and the original
source cycle. Geometric positivity alone still does not determine
the coefficient of that cycle in a quantum asymptotic expansion.
