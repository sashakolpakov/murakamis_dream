# Two contributions to the original source near the real cube

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

The real three-boundary source has two different continuations in its
asymptotic expansion. The initialized interior saddle contributes the
known dilogarithmic exponential. The ends of the full Fourier contour,
after all Fourier charges have been summed, contribute a nonzero term
of order \(N^{-3/2}\). Its exponential phase is constant.

Both contributions can be estimated on a fixed complex neighborhood of
each compact real cube. This proves a nonzero saddle coefficient on
one side of the real cube and identifies the endpoint contribution
that prevents a single saddle formula on a whole neighborhood.
No assertion places an arbitrary short-filled component in this
neighborhood.

## 1. The original source and the connection estimate

Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad
 \eta=(-1)^d,\quad \kappa=q^{d^2/2},\quad
 D_N(t)=1-\eta t^N .
 \tag{1}
\]
As in the complete generating-section and initialized-source theorems,
\[
 \mathcal C_N(\mathbf t)=
 N^{-3/2}\phi\!\left(R^3
                 \prod_{\nu=1}^3G_N(t_\nu;z)\right).
 \tag{2}
\]
Here \(\phi\) is the original Frobenius closing on
\(\mathbb C[z]/(2T_N(z/2)+2)\). All double-root derivatives are
retained; \(T_N(\cos\theta)=\cos(N\theta)\).
The polynomial \(G_N\) and the positive crossing \(R\) are the
actual finite packets, with the original normalization.

Use the holomorphic functions on the unit polydisk
\[
 \begin{aligned}
 \Psi(\mathbf t)&=-\frac{\pi}{12}
 +\frac1{2\pi}\left[
   \sum_\nu\operatorname{Li}_2(-t_\nu)
     +\operatorname{Li}_2(-t_1t_2t_3)
     -\sum_{\mu<\nu}\operatorname{Li}_2(t_\mu t_\nu)\right],\\
 B(\mathbf t)&=\prod_{\mu<\nu}(1-t_\mu t_\nu)^{-1/2},
 \qquad A_0(\mathbf t)=\prod_\nu(1+t_\nu)^{-1}.
 \end{aligned}
 \tag{3}
\]
The power-series branches at zero specify all these functions;
the square roots are positive on the real cube. Set
\[
 \Delta_N(\mathbf t)=\prod_\nu D_N(t_\nu),\qquad
 L_N=(-1)^N\kappa^3e^{-3\pi i/(4N)} .
 \tag{4}
\]

**Theorem.** For every \(0<\rho<1\), there is a fixed open complex
neighborhood \(V_\rho\) of \([-\rho,\rho]^3\), with closure in the
unit polydisk, such that
\[
 \boxed{\quad
 \frac{\mathcal C_N(\mathbf t)}{L_N\Delta_N(\mathbf t)}
 =e^{i\pi/4}B(\mathbf t)e^{iN\Psi(\mathbf t)}
       +N^{-3/2}A_0(\mathbf t)+\mathcal R_N(\mathbf t),
 \quad}
 \tag{5}
\]
where, uniformly on \(V_\rho\),
\[
 |\mathcal R_N(\mathbf t)|
 \le C_\rho\left[
       N^{-1}e^{-N\operatorname{Im}\Psi(\mathbf t)}
                         +N^{-5/2}\right].
 \tag{6}
\]
The neighborhood and constant are independent of \(N\). The estimate
holds along the full sequence, including both parities.

In particular, uniformly where
\(\operatorname{Im}\Psi\le0\) in this neighborhood,
\[
 \mathcal C_N=
 L_N\Delta_Ne^{i\pi/4}B e^{iN\Psi}(1+O_\rho(N^{-1})).
 \tag{7}
\]
This source is nonzero there for all sufficiently large \(N\).
For each fixed \(\epsilon>0\), uniformly where
\(\operatorname{Im}\Psi\ge\epsilon\),
\[
 \mathcal C_N=
 L_N\Delta_NN^{-3/2}A_0(1+O_{\rho,\epsilon}(N^{-1})).
 \tag{8}
\]
These are statements about the complete original source, rather than
an absolute-value envelope.

## 2. Analytic interpolation on a complex angular strip

The real-source proof used the explicit analytic section
\[
 U_N(t,z)=\exp\left\{\sum_{n=1}^{N-1}
 \frac{(-1)^{n+1}(2T_n(z/2)-2q^{-n})}
                    {n(e^{-2\pi in/N}-1)}\,t^n\right\}.
 \tag{9}
\]
It agrees with the actual \(G_N\), with exponentially small relative
error, at every physical value and first Casimir normal. Write
\[
 \begin{aligned}
 \Phi(t,2\cos\theta)&=
 \frac{\operatorname{Li}_2(-te^{i\theta})
      +\operatorname{Li}_2(-te^{-i\theta})
      -2\operatorname{Li}_2(-t)}{2\pi i},\\
 A(t,\theta)&=(1+2t\cos\theta+t^2)^{-1/2}.
 \end{aligned}
 \tag{10}
\]

Choose \(\rho<\rho_1<1\) and a small \(b>0\) with
\(\rho_1e^{2b}<1\). On \(|t|\le\rho_1\) and
\(|\operatorname{Im}\theta|\le2b\), the power-series logarithms
in (9)--(10) give
\[
 \log U_N(t,2\cos\theta)
       =N\Phi(t,2\cos\theta)+\log A(t,\theta)+O(N^{-1}),
 \tag{11}
\]
uniformly with every fixed number of angular derivatives.
Here and below one may reduce the strip slightly before taking
derivatives.

For completeness, expand
\[
 (e^{-2\pi in/N}-1)^{-1}
       =-\frac{N}{2\pi in}-\frac12+O(n/N)
 \qquad(n\le N/2).
 \tag{12}
\]
After substituting \(q^{-n}=e^{-\pi in/N}\), the two main series
in (9) are precisely \(N\Phi\) and \(\log A\). A fixed angular
derivative introduces at most a power of \(n\) and the factor
\(e^{2bn}\). Thus the low-frequency errors sum to \(O(N^{-1})\).
For \(N/2<n<N\), use
\[
 |e^{-2\pi in/N}-1|\ge c(N-n)/N .
 \tag{13}
\]
The remaining tails are bounded by a polynomial in \(N\) times
\((\rho_1e^{2b})^{N/2}\). This proves (11) on the stated complex
strip, without assuming continuation of a real asymptotic.

Define the phase and amplitude
\[
 \begin{aligned}
 \sigma(\theta,\mathbf t)&=
   \frac{3(\theta-\pi)^2}{4\pi}
       +\frac1i\sum_\nu\Phi(t_\nu,2\cos\theta),\\
 A_N(\theta,\mathbf t)&=
   \prod_\nu U_N(t_\nu,2\cos\theta)
                     e^{-N\sum_\nu\Phi(t_\nu,2\cos\theta)},\\
 a_N(\theta,\mathbf t)&=\sin\theta\,A_N(\theta,\mathbf t).
 \end{aligned}
 \tag{14}
\]
They are holomorphic on a common strip and parameter neighborhood.
Equation (11) gives
\[
 A_N=A_*+O(N^{-1}),\qquad
 A_*=\prod_\nu(1+2t_\nu\cos\theta+t_\nu^2)^{-1/2},
 \tag{15}
\]
in every fixed angular \(C^k\) norm there. In particular these
analytic amplitudes and their required derivatives are uniformly
bounded.

Several endpoint identities are exact for complex \(\mathbf t\):
\[
 \begin{gathered}
 \sigma(0)=\sigma(2\pi)=3\pi/4,\qquad
 \sigma'(0)=-3/2,\quad \sigma'(2\pi)=3/2,\\
 a_N(0)=a_N(2\pi)=0,\qquad
 a_N'(0)=a_N'(2\pi)=A_N(0),\\
 A_N(0)=A_0(\mathbf t)+O(N^{-1}).
 \end{gathered}
 \tag{16}
\]
They follow from \(\Phi(t,2)=0\), its dependence on
\(\cos\theta\), and (15). Reflection about \(\pi\) fixes
\(\sigma,A_N\) and negates \(a_N\).

## 3. The exact source-weighted Fourier formula

Put \(\theta_j=(2j+1)\pi/N\), \(c_j=2\cos\theta_j\),
and \(\chi_N=q^{d^2/4}\).
The calibrated physical interpolation in the real-source theorem is
\[
 R(c_j)=\chi_Ne^{iN(\theta_j-\pi)^2/(4\pi)},\qquad
 \phi(f)=(-1)^N\sum_{j=0}^{N-1}
      \left.\partial_\theta
             \{\sin\theta\,f(2\cos\theta)\}\right|_{\theta_j}.
 \tag{17}
\]
Its crossing derivative matches at every double node. The odd
simple node uses its value alone. These statements do not replace
the canonical crossing polynomial between the nodes.

The physical Hermite estimate for (9) remains exponentially accurate
on a sufficiently small complex neighborhood of the real cube.
Indeed at the real cube \(\Phi\) is purely imaginary; at complex
distance \(\delta\), its real part at physical angles is
\(O_\rho(\delta)\). Values of \(U_N\) are consequently bounded
by \(C_\rho e^{C_\rho\delta N}\), with first normals bounded
by the same factor times a fixed power of \(N\). The full physical
relative error is \(O_\rho(N^2\rho_1^N)\). Choose \(\delta\)
so small that \(e^{C_\rho\delta}\rho_1<1\). The paired source
formula (17) then bounds the total replacement error by
\(O(e^{-cN})\), after absorbing its polynomial factors.
The same argument applies to \(G_N/D_N\), since \(D_N=1+O(\rho_1^N)\).

Thus, on a fixed smaller neighborhood,
\[
 \frac{\mathcal C_N}{\Delta_N}
 =(-1)^N\chi_N^3N^{-3/2}
     \sum_j\left.\partial_\theta
       \{a_N(\theta)e^{iN\sigma(\theta)}\}\right|_{\theta_j}
                                      +O(e^{-cN}).
 \tag{18}
\]
This error is absolute. In particular it is not measured relative
to a possibly decaying saddle.

The periodic extension of
\(\partial_\theta(a_Ne^{iN\sigma})\) is continuous at the seam
and piecewise smooth, by (16). Its Fourier coefficients are
absolutely summable for each fixed \(N\). Midpoint sampling and
one integration by parts therefore give the exact identity
\[
 \sum_j\left.\partial_\theta
       \{a_Ne^{iN\sigma}\}\right|_{\theta_j}
  =\frac{iN^2}{2\pi}
       \sum_{\ell\ne0}(-1)^\ell\ell I_{\ell,N},\qquad
 I_{\ell,N}=\int_0^{2\pi}
           a_N(\theta)e^{iN(\sigma(\theta)-\ell\theta)}\,d\theta.
 \tag{19}
\]
The zero charge vanishes exactly. No endpoint or physical normal
has been removed. Reflection also gives
\[
                         I_{-\ell,N}=-I_{\ell,N}
 \tag{20}
\]
for complex parameters, with no complex conjugation.

## 4. Nonstationary charges with their endpoint coefficient

For real parameters the phase derivative \(\sigma'\) increases
from \(-3/2\) to \(3/2\), and its derivative is bounded above
and below by positive constants on the compact cube. All its
fixed derivatives are uniformly bounded. For \(|\ell|\ge2\)
write
\[
 \varphi_\ell=\sigma-\ell\theta,\qquad
 v_\ell=\varphi_\ell' .
 \tag{21}
\]
The derivative has no zero on the real interval. This persists on
a sufficiently thin complex strip and parameter neighborhood.

There is a uniform contour on which \(\varphi_\ell\) is real.
Fix a real base parameter in the compact cube and solve
\[
 \varphi_{\ell,\mathbf t}(\theta)
                    =\varphi_{\ell,\mathrm{base}}(r),
                       \qquad 0\le r\le2\pi .
 \tag{22}
\]
At the base this is \(\theta=r\). The analytic implicit function
theorem continues the solution uniformly, with displacement
\(O(\delta/(|\ell|-3/2))\). One can see uniform uniqueness by
integrating the bound
\(|\sigma'|\le3/2+o(1)<2\) on a convex thin rectangle:
the linear term \(-\ell\theta\) dominates its difference.
The endpoint phase values are fixed by (16), so the contour's
endpoints are still exactly \(0,2\pi\). This contour is homotopic
to the original interval in the analytic strip. Local parameter
neighborhoods obtained this way cover the compact real cube;
finitely many suffice, giving uniform constants.

On (22) the exponential has modulus one. Integrating by parts
three times, using \(\partial_\theta e^{iN\varphi_\ell}
=iNv_\ell e^{iN\varphi_\ell}\), proves
\[
 I_{\ell,N}=
 \frac{A_N(0)e^{3\pi iN/4}}{N^2}
  \left\{(3/2-\ell)^{-2}-(-3/2-\ell)^{-2}\right\}
                      +O(N^{-3}|\ell|^{-3})
 \quad(|\ell|\ge2).
 \tag{23}
\]
For the sign, the first boundary term vanishes since \(a_N=0\);
the second is
\(N^{-2}[a_N'e^{iN\varphi_\ell}/v_\ell^2]_0^{2\pi}\).
Both endpoint exponentials equal \(e^{3\pi iN/4}\).
The next boundary term and remaining integral have the bound
in (23). Every inverse phase derivative costs at least
\(O(|\ell|^{-1})\); the uniform strip bounds control its
derivatives and the contour lengths. Thus
\[
 \sum_{|\ell|\ge2}|\ell|\,
 \left|I_{\ell,N}-
       \frac{A_N(0)e^{3\pi iN/4}}{N^2}
        \{(3/2-\ell)^{-2}-(-3/2-\ell)^{-2}\}\right|
                                             \le CN^{-3}.
 \tag{24}
\]
This is an absolute complex estimate. It does not bound a
complex oscillatory integral by its real-parameter modulus.

## 5. The unit charges: a saddle and two endpoint rays

It suffices to treat \(\ell=1\), by (20).
At real parameters, \(\varphi_1\) is strictly convex and has
one nondegenerate critical point in \((0,2\pi)\), uniformly
separated from the endpoints. Let \(\theta_c(\mathbf t)\)
be its analytic continuation and
\(\alpha(\mathbf t)=\varphi_1(\theta_c,\mathbf t)\).
It exists on a fixed complex neighborhood. Its imaginary
part can be made uniformly small there.

Here is the contour construction that separates its saddle from
its endpoints. At a real base define
\[
 y(\theta)=\operatorname{sgn}(\theta-\theta_c)
                 \sqrt{2(\varphi_1(\theta)-\alpha)} .
 \tag{25}
\]
The quotient
\(2(\varphi_1-\alpha)/(\theta-\theta_c)^2\) is positive
on the whole real interval, including its removable value at the
critical point. Its analytic square root therefore extends to
a thin common neighborhood of that interval. Moreover \(y'\)
is positive there on the real interval. It follows that \(y\)
has a univalent holomorphic extension on a smaller neighborhood:
local invertibility is uniform by compactness, while injectivity
away from the diagonal persists from strict real monotonicity.
These properties persist for nearby complex parameters.
In this coordinate the phase is exactly
\[
                          \varphi_1=\alpha+y^2/2.
 \tag{26}
\]

The endpoint phases are the fixed real numbers
\(\beta_-=3\pi/4\), \(\beta_+=-5\pi/4\).
Their differences from the real critical value are uniformly
positive. Choose a small fixed \(h>0\) and then make the
parameter neighborhood small enough that
\(|\operatorname{Im}\alpha|<h/4\).
On each inverse branch of (26), replace the original path in
the phase plane by
\[
          \alpha\longrightarrow\alpha+ih
             \longrightarrow\beta_\pm+ih
             \longrightarrow\beta_\pm ,
 \tag{27}
\]
with the orientation reversed on the left branch.
The inverse is the positive or negative square root in (26).
For \(h\) small these paths lie in the analytic \(y\)-domain:
near the critical point their distance is \(O(\sqrt h)\);
away from it the inverse is uniformly regular. Their connectors
have imaginary phase at least \(3h/4\), and hence exponentially
small absolute integrals. This explicitly justifies the
deformation, including when the critical phase has either sign.

To evaluate the critical rays, write
\(b_N(y)=a_N(\theta(y))\,d\theta/dy\).
On \(y=\pm e^{i\pi/4}\sqrt{2s}\), the two rays combine to
\[
 \frac{e^{iN\alpha+i\pi/4}}{\sqrt2}
     \int_0^h
      \{b_N(e^{i\pi/4}\sqrt{2s})
        +b_N(-e^{i\pi/4}\sqrt{2s})\}
                       s^{-1/2}e^{-Ns}\,ds .
 \tag{28}
\]
The brace is \(2b_N(0)+O(s)\), with uniform analytic bounds.
The elementary gamma integral consequently gives
\[
 e^{iN\alpha+i\pi/4}
        \sqrt{2\pi/N}\,
        \frac{a_N(\theta_c)}{\sqrt{\sigma''(\theta_c)}}
                  +O(N^{-3/2}e^{-N\operatorname{Im}\alpha})
                  +O(e^{-cN}).
 \tag{29}
\]
The square root is fixed by its positive real value.
The truncated gamma tail is exponentially small because of
the choice \(|\operatorname{Im}\alpha|<h/4\).

On an endpoint ray use the local phase coordinate \(v=\varphi_1\).
Its amplitude is \(a_N(\theta(v))/v_1(\theta(v))\), which
vanishes at the endpoint. Its first derivative there is
\(a_N'/v_1^2\). Expanding this analytic amplitude on the vertical
ray and using
\(\int_0^h se^{-Ns}\,ds=N^{-2}+O(e^{-cN})\)
gives precisely the endpoint term in (23) with \(\ell=1\),
now with error \(O(N^{-3})\).

We have therefore proved the uniform complex expansion
\[
 \begin{aligned}
 I_{1,N}={}&
 e^{iN\alpha+i\pi/4}\sqrt{2\pi/N}\,
        \frac{a_N(\theta_c)}{\sqrt{\sigma''(\theta_c)}}\\
 &+\frac{A_N(0)e^{3\pi iN/4}}{N^2}
       \{(3/2-1)^{-2}-(-3/2-1)^{-2}\}\\
 &+O\!\left(N^{-3/2}e^{-N\operatorname{Im}\alpha}
                                   +N^{-3}+e^{-cN}\right).
 \end{aligned}
 \tag{30}
\]
The reflected charge has the opposite integral, so the source
weights in (19) make the saddle contributions add.

## 6. Summing the endpoints and restoring the original phases

Unlike a bound on the nonunit charges alone, (23) and (30)
identify the same endpoint coefficient for every charge.
Their source-weighted sum is absolutely convergent:
\[
 S(a)=\sum_{\ell\in\mathbb Z}(-1)^\ell\ell
       \{(a-\ell)^{-2}-(-a-\ell)^{-2}\},\qquad a=3/2.
 \tag{31}
\]
The combined summand is \(O(|\ell|^{-2})\).
The elementary partial-fraction identity
\[
 \sum_{\ell\in\mathbb Z}\frac{(-1)^\ell}{\ell-a}
                         =-\pi\csc(\pi a)
 \tag{32}
\]
uses symmetric limits. It follows, for example, by integrating
\(\pi\csc(\pi z)/(z-a)\) on rectangles with vertical sides at
half-integers and horizontal sides tending to imaginary infinity;
the boundary integral tends to zero, and the displayed residues
give (32). Differentiation is absolutely convergent.
Changing \(\ell\) to \(-\ell\) in one half of (31) yields
\[
 S(a)=-2\pi\csc(\pi a)
              +2a\pi^2\csc(\pi a)\cot(\pi a),\qquad
                              S(3/2)=2\pi.
 \tag{33}
\]
Thus the endpoint term does not vanish after the actual source
has summed all Fourier charges.

Inserting it into (18)--(19) gives
\[
 (-1)^N i\chi_N^3e^{3\pi iN/4}
                   \Delta_N N^{-3/2}A_N(0).
 \tag{34}
\]
The exact identity
\[
                      i\chi_N^3e^{3\pi iN/4}
                                =\kappa^3e^{-3\pi i/(4N)}
 \tag{35}
\]
turns (34) into \(L_N\Delta_NN^{-3/2}A_N(0)\), with a
positive coefficient \(+1\).
Equation (16) replaces \(A_N(0)\) by \(A_0\) with error
\(O(N^{-5/2})\) after normalization. The remainders in
(24) and (30) have the same order after multiplication by
the source factor \(N^{1/2}\).

For the saddle, the identities established on the real cube
continue holomorphically to this neighborhood:
\[
 \begin{gathered}
 \theta_c=2\pi-\theta_*,\qquad
 2\cos\theta_*=1-\frac{t_1+t_2+t_3+
                      t_1t_2+t_1t_3+t_2t_3}{1+t_1t_2t_3},\\
 \alpha=\Psi+3\pi/4-2\pi,\qquad
 \frac{2\sin\theta_*\,A_*(\theta_*)}
                 {\sqrt{\,2\pi\sigma''(\theta_*)\,}}=B .
 \end{gathered}
 \tag{36}
\]
The analytic critical branch and square roots are fixed at the
real cube; its critical points remain distinct from the endpoints.
The real action and amplitude identities imply (36) in the
complex neighborhood by the identity theorem in each variable.
Replacing \(A_N\) by \(A_*\) in (29) costs
\(O(N^{-1}|e^{iN\Psi}|)\) after source normalization.
Equations (19)--(20), (29), and (35)--(36) then give the
first term of (5), with its displayed coefficient.

The remaining absolute exponential errors can be absorbed in
\(O(N^{-5/2})\). This proves (5)--(6).
Because \(A_0\) and \(B\) are uniformly bounded above and away
from zero after shrinking the neighborhood, (7)--(8) follow.

## 7. Why a whole-neighborhood single saddle formula fails

The endpoint branch is visible immediately on one side of every
real point. To verify that the two sides really occur, at a real
point write
\[
 z_*=2\cos\theta_*\in(-2,2),\qquad
 b_i=1+t_i z_*+t_i^2 .
 \tag{37}
\]
The envelope derivative of the initialized action is
\[
 \partial_{t_i}\Psi=
 \frac{\log b_i-2\log(1+t_i)}{2\pi t_i}<0.
 \tag{38}
\]
For \(t_i\ne0\), its sign follows from
\(b_i/(1+t_i)^2=1+t_i(z_*-2)/(1+t_i)^2\).
At \(t_i=0\), its continuous value is
\((z_*-2)/(2\pi)<0\).

Moving a small fixed distance in a negative imaginary coordinate
direction therefore gives \(\operatorname{Im}\Psi>0\).
At each such fixed point the first term of (5) decays exponentially,
whereas the actual source has the nonzero endpoint asymptotic (8).
Consequently no fixed complex neighborhood of any real point
supports the single-saddle relative formula (7) throughout.
On the opposite side, (7) proves that the initialized saddle
coefficient is nonzero without assigning it by hand.

The connection estimate does not decide cancellation in the
shrinking transition region where the two terms have comparable
size. It neither asserts zero-freeness on all \(V_\rho\) nor
extends the result to the whole unit polydisk. No derivative
estimate for the relative one-saddle remainder is inferred.

## 8. Scope and complete proof sources

This is a fixed-root statement with the actual first Casimir
normals, both parities, the odd simple node, and every displayed
normalizing factor retained. The endpoint is a contribution to the
same initialized source, not a change of closing or a discarded
alias. The uniform complex estimate is obtained by explicit contour
deformation; it is not inferred from holomorphy of a real asymptotic.

The result supplies a source-sensitive complex packet on
\(\operatorname{Im}\Psi\le0\) near the real cube and the
connection to its endpoint contribution. Establishing the required
geometric parameter domain, the assembled coefficient cycle, and
a nonzero original coefficient after arbitrary fixed short fillings
remains separate. No volume identity is proved here.

All three complete proof texts were read at their matching pins:

| Source | SHA-256 |
|---|---|
| [Real initialized source](research_centered_tensor_real_source_packet.md) | 4052f55915ff8d9688de9b714f8209eab4c7ea885467024c864cc9c68e07e654 |
| [Full generating section and normals](research_full_degree_centered_generating_section.md) | 6fbef2085aca79503518745a08d3466ec84cd337ec8131944e2aebb9c95c2f6b |
| [Initialized finite source](research_centered_tensor_finite_6phi5_source.md) | 238b5fd4daeca0293ae705d1a4c1189824129a0278e086e250207e8d51ed3f53 |

No novelty is claimed for analytic Morse coordinates, contour
deformation, Gaussian or endpoint asymptotics, or partial fractions
of the cosecant. The additional source-specific statements are the
uniform two-contribution estimate, the nonzero fully summed endpoint
coefficient, and the resulting complex-side distinction.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git operation
or earlier-final edit was performed.
