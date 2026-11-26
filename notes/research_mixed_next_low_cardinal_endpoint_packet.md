# The cumulative low-cardinal row and its outgoing phase

Research deduction, 7 November 2026. Before the maximum of the original
three-crossing Fourier profile, the cumulative coefficient in the
first-node sector has a complete nonzero endpoint asymptotic. Its
coefficient simplifies to a rational function of the original
quadratic root. The absolute action is an original type-four
conditional action with its outgoing argument at the seam.

This supplies the actual row symbol for the remaining coherent
outgoing sum. It does not estimate that complete sum or supply a
contour deformation for the discrete cumulative coefficients.
No numerical evaluation is used.

## 1. Exact coefficients and the uniform endpoint sum

Keep all notation and exact sources from
[the low-cardinal coherent response](research_mixed_next_low_cardinal_coherent_response.md).
In particular
\[
 \begin{gathered}
 D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
 \kappa=q^{D^2/2},\quad P_j=(r;r)_j,\quad S_j=|P_j|,\\
 \gamma=MJM^3e_0,\qquad v_j=(-q)^{-j}\gamma_j,\qquad
 a_j=\frac1{P_j}\operatorname{CT}_Y
       \left[\frac{d_N(Y)-1}{Y-1}\,Y^{-j}p_j(Y)\right].
 \end{gathered}
 \tag{1}
\]
The apparent quotient is a polynomial. The original complete
first-node sectors have the exact coefficient forms
\[
 \mathcal S_{1,\beta}[\mathfrak l_0](Z)
     =\sum_{j=0}^{D}a_j\,\frac{p_j(Z)}{P_j^{1+\beta}},
 \qquad
 \mathcal S_{0,\beta}[\mathfrak l_0](Z)
     =\sum_{j=0}^{D}(1-a_j)\frac{p_j(Z)}{P_j^{1+\beta}}.
 \tag{2}
\]
The retained increment is
\[
 a_0=1-\frac{\gamma_0}{\kappa^2N^2},\qquad
 a_j-a_{j-1}
   =-\frac1{\kappa^2N^2}
       \left(v_j+\frac{r^j}{1-r^j}v_{j-1}\right).
 \tag{3}
\]

For \(0<t<1/2\), set
\[
 \begin{split}
 X(t)&=e^{-2\pi it},\qquad d_*(t)=4\sin^2\pi t,\\
 \lambda(t)&=\frac{3-2X(t)+\sqrt{4/X(t)-3}}2,\qquad
 I(t)=\int_0^t\log\lambda(s)\,ds,\\
 G(t)&=\sqrt{\frac{\lambda(t)}{\lambda(t)-\mu(t)}},\qquad
 \mu(t)=\frac{3-2X(t)-\sqrt{4/X(t)-3}}2,\\
 J(t)&=\int_0^t\log(2\sin\pi s)\,ds,\qquad
 A(t)=\Re I(t)-2J(t).
 \end{split}
 \tag{4}
\]
All branches are those of
[the original Fourier-column theorem](research_three_crossing_next_crossing_fourier.md),
continued from \(\sqrt{4/X-3}=1\), \(\log\lambda=0\), and \(G=1\)
at zero. Let \(x_*\in(1/3,1/2)\) be its unique real maximum of \(A\).
Thus \(A'>0\) on \((0,x_*)\) and \(A(0)=0\).

Fix any constants
\[
                         0<a<b<x_*.
 \tag{5}
\]
The original source theorem supplies the complete nonzero packet
\[
 v_j=\gamma_0 S_j^{-2}G(j/N)e^{NI(j/N)}
                          (1+O_b(N^{-1})),
                   \qquad 0\le j\le bN.
 \tag{6}
\]
This includes the true endpoint normalization and its forcing.
Define
\[
 \rho(t)=d_*(t)/\lambda(t),\qquad
 B(t)=1-\frac{1-X(t)}{\lambda(t)}.
 \tag{7}
\]
On every compact subinterval of \((0,x_*)\), \(|\rho|<1\),
and \(B\ne0\). The latter follows by substitution of
\(\lambda=1-X\) in its characteristic polynomial, giving
\(-(1-X)/X\ne0\), as proved in the coherent-response note.

**Theorem 1.** Uniformly for all physical \(j\) with
\(a\le j/N\le b\), at both parities,
\[
 \boxed{\quad
 a_j=-\frac{v_j}{\kappa^2N^2}
         \frac{\lambda(j/N)-1+X(j/N)}
              {\lambda(j/N)-d_*(j/N)}
                 (1+O_{a,b}(N^{-1})).
 \quad}
 \tag{8}
\]
In particular the leading coefficient is nonzero.

*Proof.* Put \(k_0=\lfloor aN/2\rfloor\). For
\(k_0\le k\le bN\), divide consecutive nonzero formulas (6).
They give, uniformly,
\[
 \frac{v_{k-1}}{v_k}=\rho(k/N)+O(N^{-1}),\qquad
 v_k+\frac{r^k}{1-r^k}v_{k-1}
                          =v_k\{B(k/N)+O(N^{-1})\}.
 \tag{9}
\]
For large \(N\), the modulus of the first ratio is at most a
fixed \(q_0<1\), since the interval is separated from zero
and \(x_*\).

The portion \(k<k_0\) is estimated before dividing by \(v_j\).
The uniform endpoint packet (6), the uniform sine-factorial
estimate, and monotonicity of \(A\) imply
\[
 |v_k|\le C N^C e^{NA(a/2+1/N)}\qquad(k<k_0).
 \tag{10}
\]
For \(1\le k<N\), \(|1-r^k|^{-1}\le N/4\).
Thus this whole early part of the sum (3), including \(a_0\),
is polynomially bounded times the rate in (10).
For \(j/N\ge a\), (6) and the compact factorial asymptotic
give
\[
 |v_j|\ge cN^{1/2}e^{NA(j/N)}.
 \tag{11}
\]
Since \(A(a)>A(a/2)\), the early contribution is exponentially
small compared with \(v_j/N^2\), uniformly in (5).

It remains to sum the late part backwards. Write \(t=j/N\)
and \(k=j-\ell\). By (9), the smoothness of \(\rho\), and
the product telescoping identity,
\[
 \frac{v_{j-\ell}}{v_j}
       =\rho(t)^\ell+
                  O\!\left(\frac{(\ell+1)^2}{N}q_1^{\ell-1}\right)
 \tag{12}
\]
for some fixed \(q_1<1\), as long as \(j-\ell\ge k_0\).
To justify this estimate uniformly even for large \(\ell\),
bound every factor in the product and its comparison factor
by \(q_1\); the difference at the \(m\)-th position is at most
\(C(m+1)/N\). Sum the resulting \(\ell\) telescoping terms.
The harmless case \(\ell=0\) is interpreted separately.
Also \(B(t-\ell/N)=B(t)+O(\ell/N)\).
The convergent sums of \(\ell q_1^\ell\) and
\(\ell^2q_1^\ell\) therefore show
\[
 \sum_{k=k_0}^{j}
  \frac{v_k}{v_j}\{B(k/N)+O(N^{-1})\}
            =\frac{B(t)}{1-\rho(t)}+O(N^{-1}).
 \tag{13}
\]
Extending the finite geometric comparison to infinity costs an
exponentially small tail, since \(j-k_0\ge aN/2-O(1)\).
Substitute (13) in (3), and use the early-part estimate.
Finally
\[
 \frac{B(t)}{1-\rho(t)}
       =\frac{\lambda(t)-1+X(t)}{\lambda(t)-d_*(t)}.
 \tag{14}
\]
This quotient is bounded away from zero on (5), so the error
can be written relatively. This proves (8). \(\square\)

## 2. The rational root and the original seam-conditional action

Put
\[
 u(t)=\frac{1-\sqrt{4/X(t)-3}}2,\qquad
 D(u)=1-u+u^2.
 \tag{15}
\]
On this branch the following identities are exact:
\[
 X=\frac1{D(u)},\quad
 \lambda=\frac{(1-u)^3}{D(u)},\quad
 d_*=-\frac{u^2(1-u)^2}{D(u)},\quad
 1-X=-\frac{u(1-u)}{D(u)}.
 \tag{16}
\]
Consequently
\[
 \lambda-1+X=1-u,\qquad
 \lambda-d_*=(1-u)^2,\qquad
 \frac{\lambda-1+X}{\lambda-d_*}=\frac1{1-u}.
 \tag{17}
\]
None of the denominators in these identities vanishes on
the real interval (5).

The exact moment identification has an additional source meaning:
\[
 C_{1,N}(r^j,1)
      =\frac{N M_j}{P_j}
      =\frac{v_j}{\kappa^2N}.
 \tag{18}
\]
The first equality follows from the full finite definition:
at the physical incoming node,
\[
 C_{1,N}(r^j,1)
       =\frac1{P_j}
           \sum_{k=0}^{D-j}
               \frac{r^{-jk}P_{k+j}}{P_k^2}.
 \tag{19}
\]
Thus Theorem 1 is equivalently
\[
 a_j=-\frac{C_{1,N}(r^j,1)}{N(1-u(j/N))}
                                      (1+O_{a,b}(N^{-1})).
 \tag{20}
\]
It concerns the complete original conditional source at its outgoing
seam, with no row deletion from (19).

For an absolute action calibration, let \(g\) be the original
negative-root factorial primitive,
\[
 g(z)=J(z)+\frac{i\pi}{2}(z-z^2),\qquad
 g'(z)=\log(1-e^{-2\pi iz})
 \tag{21}
\]
on \(0<\Re z<1\), with the original logarithmic continuation.
For real \(0<t<1/2\), \(u(t)\) has negative imaginary part.
Define \(s(t)\) by \(e^{-2\pi is(t)}=u(t)\) and
\(0<\Re s(t)<1/2\). Both \(s\) and \(s+t\) are in the
original regular strips. The literal phase of (19) is
\[
 \Phi(s;t)=g(s+t)-2g(s)-g(t)+2\pi its.
 \tag{22}
\]
Its exponentiated inner equation is
\[
                 1-Xu=X(1-u)^2,
 \tag{23}
\]
which follows from (16).

This equation has the zero original logarithmic lift at \(s(t)\).
For completeness, if \(\sigma=\Re s\), the original argument
\(\Im g'(x+ih)\) lies between \(0\) and
\(\pi(1-2x)\), with the endpoints ordered according to their sign.
The inequalities are strict unless \(x=1/2\), when the argument
is zero.
This follows directly from \(1-e^{2\pi h}e^{-2\pi ix}\).
Consequently, for \(0<\sigma,t<1/2\), \(\sigma+t<1\),
\[
                        -2\pi<\Im\Phi_s<\pi.
 \tag{24}
\]
Indeed, if \(\sigma+t\le1/2\), the lower bound is
\(-2\pi+4\pi\sigma+2\pi t\) and the upper bound is
\(\pi-2\pi\sigma\). If \(\sigma+t>1/2\), the corresponding
bounds are \(-\pi+2\pi\sigma\) and \(2\pi t\).
By (23) the derivative is an integral multiple of \(2\pi i\);
(24) leaves only zero.

Write \(\mathcal H(t)=\Phi(s(t);t)\). Differentiating with the
inner derivative zero gives
\[
 \exp\mathcal H'(t)
   =\frac{1-Xu}{(1-X)u}
   =\frac{\lambda(t)}{d_*(t)}.
 \tag{25}
\]
The equality of logarithms has no extra charge. The real and
imaginary parts of \(\lambda(t)\) are positive for \(0<t<1/2\),
so \(\Im\log\lambda\in(0,\pi/2)\). On the original strips,
\[
 -\pi/2<\Im\mathcal H'(t)<\pi.
 \tag{26}
\]
To see this directly, use
\(\Im g'(t)=\pi/2-\pi t\) and the same two cases
\(\sigma+t\le1/2\) or \(>1/2\) in
\(\mathcal H'=g'(s+t)-g'(t)+2\pi is\).
Their difference of logarithmic lifts is therefore zero. Hence
\(\mathcal H'=I'-2J'\).

Finally \(u(t)\sim-2\pi it\) as \(t\downarrow0\).
Thus \(s(t)\) goes down the original strip, with bounded real part,
and \(t s(t)\to0\). The original lower-half primitive has
\(g(s)\to i\pi/12\) there. This is the fixed constant in
the disk formula of
[Fourier-weight continuation](research_mixed_fourier_weight_continuation.md),
equation (22). It follows from (22) that
\[
 \boxed{\qquad
       \mathcal H(t)=I(t)-2J(t)-\frac{i\pi}{12}.
 \qquad}
 \tag{27}
\]
This fixes the absolute action, not merely its exponentiated derivative.

## 3. The nonzero row symbol and its critical curve

The actual endpoint scalar is also fixed by the old source:
\[
 \frac{\gamma_0}{\kappa^2}
        =N^{3/2}\omega_N(1+O(N^{-1})),\qquad
 \omega_N=\exp i\pi\left(\frac14+\frac1{4N}-\frac N{12}\right).
 \tag{28}
\]
Indeed the original endpoint theorem gives
\(\gamma_0=\kappa^4(-1)^Nq^{-1}\omega_N N^{3/2}
+O(N^{1/2})\), and
\((-1)^N\kappa^2q^{-1}=1\) at both parities.
Combining (6), (8), (17), the sine-factorial asymptotic, and
(27)--(28) proves
\[
 a_j=-e^{i\pi/4}N^{-3/2}
       \frac{G(t)}{2\sin(\pi t)(1-u(t))}
                e^{N\mathcal H(t)}(1+O_{a,b}(N^{-1})),
                  \qquad t=j/N.
 \tag{29}
\]

Let \(Z=e^{-2\pi iz}\), and let \(z\) range over any compact
set for which \(z\) and \(t+z\) stay in their original regular
strips for all \(t\in[a,b]\). In particular this permits the
actual next-reference output sets, whose real parts lie in
\((0,1/2)\). Set
\[
 \mathfrak a(z)=\sqrt{2\sin\pi z}\,e^{-\pi iz/2},\qquad
 \Theta_\beta(t,z)
     =\mathcal H(t)+g(t+z)-g(z)-(1+\beta)g(t).
 \tag{30}
\]
The square roots are their original continuations.
The full literal outgoing row in the first line of (2) then obeys
\[
 \boxed{\quad
 a_j\frac{p_j(Z)}{P_j^{1+\beta}}
       =N^{-2-\beta/2}\,\mathcal B_\beta(t,z)
              e^{N\Theta_\beta(t,z)}(1+O(N^{-1})),
 \quad}
 \tag{31}
\]
where the nonzero coefficient is
\[
 \mathcal B_\beta(t,z)
   =-\frac{e^{i\pi/4}G(t)}{2\sin(\pi t)(1-u(t))}
      \frac{\mathfrak a(t+z)}
           {\mathfrak a(z)\mathfrak a(t)^{1+\beta}}.
 \tag{32}
\]
The estimate is uniform in the stated physical index interval
and on those output compacts. Fixed outgoing derivatives follow
from the same uniform holomorphic factorial packets and Cauchy.
It asserts no incoming-index derivatives of the discrete \(a_j\).

Since \(A(t)>0\) on (5), (29) also implies
\(1-a_j=-a_j(1+O(e^{-cN}))\), with some \(c>0\) after
absorbing powers of \(N\). Thus the second line of (2) has
the same row phase and the opposite leading coefficient on this
interval. Their exact coefficientwise sum is still one.

The analytically continued row phase has the exponentiated equation
\[
 \exp\partial_t\Theta_\beta
      =\frac{\lambda(t)}{d_*(t)}
          \frac{1-XZ}{(1-X)^{1+\beta}}.
 \tag{33}
\]
Therefore every regular critical point must satisfy
\[
           \lambda(1-XZ)=d_*(1-X)^{1+\beta}.
 \tag{34}
\]
Using (16), its original quadratic sheet has the rational
parametrizations
\[
 \boxed{\begin{split}
 \beta=0:\quad &Z=D(u)-u^3=(1-u)(1+u^2),\\
 \beta=1:\quad &Z=D(u)+\frac{u^4(1-u)}{D(u)}.
 \end{split}}
 \tag{35}
\]
Equivalently elimination of \(\lambda\) gives
\[
 (1-X)^{3+2\beta}
  +X(3-2X)(1-X)^\beta(1-XZ)
  -X(1-XZ)^2=0.
 \tag{36}
\]
For \(\beta=0\) this simplifies to
\[
        1-X+(1-Z)X^2-(1-Z)^2X^3=0.
 \tag{37}
\]
Equations (35)--(37) are necessary regular equations on the
specified sheet. They do not admit zeros of the displayed
denominators, establish the logarithmic lift in the outer variable,
or prove that a critical point contributes.

More explicitly, the logarithmic differentials on this sheet have
the rational multipliers
\[
 \exp\Theta_{0,t}=\frac{D(u)-Z}{u^3},\qquad
 \exp\Theta_{1,t}=-\frac{D(u)\{D(u)-Z\}}{u^4(1-u)},\qquad
 dt=\frac{D'(u)}{2\pi iD(u)}\,du.
 \tag{38}
\]
Their logarithms retain the original continuation in (30).
The rational expressions do not extend Theorem 1 automatically
past its strict geometric-ratio region. In particular the
\(\lambda\) cover has a turning point at \(u=1/2\), where
\(D'(u)=0\) and \(X=4/3\); the simplification (17) does not
remove that turning point from the original column source.

## 4. What source has actually been identified

Equation (18) identifies the complete inner response with
\(C_{1,N}(r^j,1)\), and (27) identifies its absolute seam action.
The outgoing seam \(1\), or logarithmic coordinate zero, is not
an ordinary plateau neighbor in the canonical conditional-image
theorems. Those theorems therefore do not supply an outer
contour estimate for (2). The nonzero inner asymptotic here comes
instead from the original \(\gamma\) theorem and the exact
cumulative sum.

Theorem 1 evaluates the whole cumulative response defining each
\(a_j\) in (5); it is not just an adjacent-row lower bound.
However the complete coherent \(j\)-sum still includes the
complementary index ranges and its original two-sector cancellation.
A deformation of that sum needs a valid finite-source interpolation
and all its joining and alias terms. The row formula alone does not
provide such an interpolation or a whole-sector upper bound.

All formulas retain the original phases, endpoint forcing and
both level parities. They can be inserted into the exact low-prefix
formula (29) of the coherent-response note without changing its
\(\kappa^{-2}N^{-1}\), its full ordinary coefficient
\(\ell_{b,N}(w)\), or any boundary normal.
