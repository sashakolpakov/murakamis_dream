# The full complete-boundary coefficient in the contracted basis

Research proof, 4 November 2026. The frozen manuscripts are unchanged.

The complete boundary vector in the mixed three/four formula contains a
one-dimensional oscillatory sum. Its stationary point was identified in
[the complete-boundary calculation](research_mixed_complete_boundary_sum.md),
but that calculation did not prove that the point contributes to the
whole sum. We prove that assertion here, uniformly on every compact
interval of regular real outer indices. The proof keeps both level
parities and every fixed ordinary derivative of the boundary color.

This is a theorem about the actual boundary coefficient. It does not
estimate the coupled interior sum of an arbitrary mixed word.

## 1. The coefficient and its asymptotic

For an integer level \(N\ge2\), set
\[
 q=e^{\pi i/N},\qquad S_l=\prod_{a=1}^l2\sin(\pi a/N),\qquad
 \delta_j=\exp\!\left(\frac{\pi i}{2N}((N-1)j-j^2)\right).
 \tag{1}
\]
The empty product is one. Let
\[
 e_l(w)=\frac{\prod_{a=0}^{l-1}(2\cos((2a+1)\pi/N)-w)}{S_l^2},
 \qquad E_{l,k}=(-1)^k e_l^{(k)}(-2).
 \tag{2}
\]
The exact change of basis gives
\[
 b_{j,N}^{(k)}(-2)=(-1)^k\delta_j^{-1}
       \sum_{l=0}^j q^{jl}\frac{E_{l,k}}{S_lS_{j-l}}.
 \tag{3}
\]
Here \(b_{j,N}^{(k)}\) is the ordinary \(k\)-th derivative of the
original transformed boundary vector; it is not a derivative in \(j\).
Formula (3) is proved in Lemma 1 of the complete-boundary calculation.

Use the holomorphic primitive
\[
 J(z)=\int_0^z\Log(2\sin\pi v)\,dv
 \quad(0<\Re z<1),
\]
continued from \(0<z<1\), and put
\[
 \begin{split}
 V_0(u)&=-2J(1/2-u)-2J(u),\\
 B(e,u)&=V_0(u)-J(u)-J(e-u),\\
 F(e,u)&=B(e,u)+i\pi eu,\qquad 0<\Re u<e<1/2.
 \end{split}
 \tag{4}
\]
For real \(0<e<1/2\), the unique critical point in this strip is
\[
 \begin{split}
 X&=e^{2\pi i e},\qquad
 z=\frac{i+\sqrt{1-2X}}2,\qquad u_c(e)=\pi^{-1}\arctan z,\\
 0&<\Re u_c<\min(e,1/4),\qquad H(e):=\Im u_c>0.
 \end{split}
 \tag{5}
\]
The square root has positive real and negative imaginary parts; the
arctangent is continued from \(e\downarrow0\). Proposition 4 of the
complete-boundary calculation proves \(F_u(e,u_c)=0\) with the actual
logarithmic lift, not just its exponentiated equation.

**Theorem 1.** Fix a compact interval \(I\subset(0,1/2)\) and an integer
\(k\ge0\). Uniformly for all integer pairs \(N,j\) with \(j/N\in I\),
\[
 b_{j,N}^{(k)}(-2)=(-1)^k\delta_j^{-1}N^{k-3/2}
     A_k(e)e^{NF(e,u_c(e))}\{1+O_{I,k}(N^{-1})\},
 \qquad e=j/N,
 \tag{6}
\]
where
\[
 A_k(e)=\frac{\sqrt{2\pi}}{\sqrt{-F_{uu}(e,u_c)}}
 \frac{\bigl(\tan(\pi u_c)/(4\pi)\bigr)^k}
 {(2\sin\pi u_c)^{3/2}(2\sin\pi(e-u_c))^{1/2}}\ne0.
 \tag{7}
\]
All square roots continue from the positive sine roots in the real
strip. The Gaussian square root has positive real part, since
\(\Re[-F_{uu}(e,u_c)]>0\). In particular (6) is an asymptotic for
the whole finite sum (3), not only a selected local integral.

## 2. Exact interpolation and ordinary boundary derivatives

Let \(G_N\) be the sine-factorial interpolation in
[the factorial construction](exact_factorial_interpolation_and_complex_contours.md).
It satisfies \(G_N(l)=S_l\),
\(G_N(v+1)=2\sin(\pi(v+1)/N)G_N(v)\), and
\(G_N(v)G_N(N-1-v)=N\). Write \(c=(N-1)/2\). Then
\[
 \mathcal E_N(u,t)=
 \frac{N}{G_N(Nu)^2
 G_N(c-Nu+Nt/(2\pi))G_N(c-Nu-Nt/(2\pi))}
 \tag{8}
\]
equals \(e_l(-2\cos t)\) at \(u=l/N\). This exact identity is also
recorded in Section 3 of
[the uniform factorial bounds](research_uniform_factorial_and_boundary_decay.md).
For completeness, the quotient of the expressions for \(l+1\) and
\(l\) is
\[
 \frac{4\cos(\pi(l+1/2)/N+t/2)
              \cos(\pi(l+1/2)/N-t/2)}{4\sin^2(\pi(l+1)/N)}
 =\frac{2\cos((2l+1)\pi/N)+2\cos t}
              {4\sin^2(\pi(l+1)/N)},
\]
and the value at \(l=0\) is one by reflection. Thus no unspecified
periodic factor enters (8).

For \(u\) in a compact subset of \(0<\Re u<1/2\) and sufficiently
small complex \(t\), the factorial expansion gives
\[
 \mathcal E_N(u,t)=\frac{1}{2N\sin\pi u}
       e^{N V(u,t)}\{1+O(N^{-1})\},
\]
\[
 V(u,t)=-2J(u)-J(1/2-u+t/(2\pi))-J(1/2-u-t/(2\pi)).
 \tag{9}
\]
The normalized error is holomorphic and uniform, with each fixed
derivative on a smaller compact set. Indeed
\(G_N(Nx-1/2)=\sqrt N e^{NJ(x)}(1+O(N^{-1}))\);
the two midpoint factors therefore introduce no further leading
coefficient. Both sides of (8) are even in \(t\), so they are
holomorphic in the ordinary color \(w=-2\cos t\) near \(-2\).
Since
\[
 \partial_w V(u,t)\big|_{w=-2}
       =-\frac{\tan\pi u}{4\pi},
 \tag{10}
\]
differentiation yields an exact interpolation \(\mathcal E_{N,k}\)
of \(E_{l,k}\), with
\[
 \mathcal E_{N,k}(u)=
 N^{k-1}\frac{(\tan\pi u/(4\pi))^k}{2\sin\pi u}
          e^{NV_0(u)}\{1+O(N^{-1})\}.
 \tag{11}
\]
The leading factor does not vanish in this strip. Dividing by
\(G_N(Nu)G_N(N(e-u))\) and multiplying by \(e^{i\pi Neu}\)
gives an exact holomorphic summand \(f_{N,k}(e,u)\). Uniformly on
regular compact sets,
\[
 f_{N,k}(e,u)=N^{k-2}a_k(e,u)e^{NF(e,u)}(1+O(N^{-1})),
\quad
 a_k=\frac{(\tan\pi u/(4\pi))^k}
 {(2\sin\pi u)^{3/2}(2\sin\pi(e-u))^{1/2}}.
 \tag{12}
\]
This proves the complex symbol needed in the deformation below.

## 3. The full endpoint gap

The following comparison is the reason the local stationary point
can be used for the complete sum. For horizontal differentials,
\[
 -\Re F_{uu}(e,u)=\pi\Re\{2\tan\pi u+3\cot\pi u+
                                    \cot\pi(e-u)\}>0
 \tag{13}
\]
throughout \(0<\Re u<e<1/2\), at every finite height. Thus on
\(\Im u=H(e)\) the real phase has a unique maximum at \(u_c(e)\).
Its boundary values at \(iH\) and \(e+iH\) are strictly smaller.

We must also compare the vertical sides with the real endpoints.
The derivative is
\[
 F_u=2\Log\cos\pi u+\Log\sin\pi(e-u)
                   -3\Log\sin\pi u+i\pi e.
 \tag{14}
\]
The constants in the logarithms cancel. For \(u=iy, y>0\),
the cosine has argument zero, the first sine has argument in
\((-\pi/2,0)\), and \(\arg\sin\pi u=\pi/2\).
Consequently \(\Im F_u<0\). At \(u=e+iy\), the cosine has
negative argument, \(\arg\sin\pi(e-u)=-\pi/2\), and the
remaining sine has positive argument; again
\(\Im F_u< -\pi/2+\pi e<0\). Hence
\[
 \partial_y\Re F(e,iy)>0,\qquad
 \partial_y\Re F(e,e+iy)>0.                         \tag{15}
\]
The phase has finite continuous limits at the two real endpoints.
It follows from (13)--(15) that both entire vertical segments,
including their real endpoints, lie strictly below
\(\lambda(e):=\Re F(e,u_c(e))\).

By compactness of \(I\), choose \(\varepsilon>0\) and
\(\delta>0\) uniformly so that:

* the critical point lies strictly between the cuts
  \(\varepsilon\) and \(e-\varepsilon\);
* on the two vertical segments above these cuts, up to height \(H(e)\),
  the phase is at most \(\lambda(e)-\delta\);
* on the real endpoint intervals \([0,\varepsilon]\) and
  \([e-\varepsilon,e]\), the same strict bound holds.

The limiting lines \(\Re u=0,e\) are used only for this comparison.
Every contour used below stays inside the regular strip. The uniform
real factorial estimate, including its endpoint logarithms, bounds
the omitted original terms by
\(N^C e^{N(\lambda(e)-\delta)}\). This remains true for each
fixed \(k\): differentiating a finite product changes its uniform
real upper bound by a power of \(N\), as proved in (10) of the
complete-boundary calculation.

## 4. Exact summation, aliases, and the nonzero coefficient

Replace the two interior cuts by half-grid cuts within \(O(N^{-1})\).
Take a rectangle with those vertical sides and horizontal heights
\(\pm H(e)\). The kernel
\[
                  K_N(u)=\frac{1}{1-e^{-2\pi iNu}}
 \tag{16}
\]
has residue \(1/(2\pi iN)\) at every enclosed lattice point. Thus
\(N\oint K_N f_{N,k}\,du\) is exactly the retained finite sum.
On the lower horizontal side write \(K_N=1+(K_N-1)\); on the
upper side \(K_N=O(e^{-2\pi NH})\). Cauchy's theorem transfers
the integral of \(f_{N,k}\) from the lower side to the upper side,
leaving the upper horizontal integral with coefficient \(N\), the
two upper vertical integrals, and exponentially weighted aliases.
This retains all contour segments, rather than dropping an endpoint
term in a formal Poisson expansion.

For real \(e\), the phase has the exact reflection relation
\[
 \Re F(e,x-iy)=\Re F(e,x+iy)+2\pi ey.               \tag{17}
\]
On the lower horizontal side the factor \(K_N-1\) supplies
\(e^{-2\pi NH}\); therefore its rate is at most
\(\lambda(e)-2\pi(1-e)H(e)\). The upper alias has rate at most
\(\lambda(e)-2\pi H(e)\). Both losses are uniformly positive
on \(I\).

The same estimate controls the lower vertical aliases. At a half-grid
cut, for \(y\ge0\),
\[
 |K_N(x+iy)|\le e^{-2\pi Ny},\qquad
 |K_N(x-iy)-1|\le e^{-2\pi Ny}.
 \tag{18}
\]
Combine (17)--(18) with the strict upper vertical bound from Section 3.
The remaining upper vertical integrals have that bound directly.
The \(O(N^{-1})\) changes of the cuts preserve every fixed gap.
All interpolation coefficients and derivatives contribute only fixed
powers of \(N\) on these regular compact rectangles.

It remains to evaluate the upper horizontal integral. Its unique
maximum is the simple critical point \(u_c\), and (13) gives a
uniform quadratic loss away from it. The holomorphic expansion (12)
and one-dimensional Gaussian integration yield
\[
 N\int f_{N,k}(e,x+iH(e))\,dx
 =N^{k-3/2}\frac{\sqrt{2\pi}\,a_k(e,u_c)}
                         {\sqrt{-F_{uu}(e,u_c)}}
       e^{NF(e,u_c)}(1+O(N^{-1})).                  \tag{19}
\]
The odd first Gaussian correction integrates to zero. Every discarded
term and every additional contour piece is exponentially smaller.
Multiplying by the exact factor in (3) proves Theorem 1.

## 5. The resulting difference transport

This full-sum theorem also gives an almost-invariance statement for the
boundary vector, with its nontrivial phase retained. Put
\(U(e)=e^{2\pi i u_c(e)}\) and \(X(e)=e^{2\pi i e}\).
For neighboring physical indices remaining in a fixed compact
subinterval of \((0,1/2)\), Theorem 1 implies
\[
 \frac{b_{j+1,N}(-2)}{b_{j,N}(-2)}
       =R(e)\{1+O(N^{-1})\},\qquad
 R(e)=\frac{X(e)U(e)}{X(e)-U(e)},\quad e=j/N.
 \tag{20}
\]
Indeed, writing \(S(e)=F(e,u_c(e))\), stationarity gives
\[
 S'(e)=-\Log(2\sin\pi(e-u_c))+i\pi u_c,\qquad
 \frac{\delta_j}{\delta_{j+1}}=-i e^{i\pi(e+1/N)}.
\]
Taking the ratio of (6) at adjacent indices proves (20), including
its phase. The exponentiated endpoint equation gives the exact
algebraic relations
\[
 (1+U)^2(X-U)=(1-U)^3,\qquad
 X=\frac{5U^2-2U+1}{(1+U)^2}.
 \tag{21}
\]
The selected branch has \(|U|<1\), so none of the denominators in
(20)--(21) vanishes. In particular
\[
 |b_{j+1,N}(-2)-R(j/N)b_{j,N}(-2)|
       \le \frac{C_I}{N}|b_{j,N}(-2)|.
 \tag{22}
\]
Thus approximate difference transport here follows from a proved
asymptotic of the actual boundary vector. Its multiplier is algebraic
in the original index exponentials. This is not an almost-invariant
vector for every interior crossing operator, nor does the relative
error in (22) control an exponentially small closing observation of
an arbitrary word.

## 6. Scope and reproduction

The theorem proves a nonzero leading coefficient for an entire
original one-dimensional sum, uniformly for \(j/N\) in any fixed
compact subset of \((0,1/2)\). It also supplies the corresponding
ordinary boundary derivatives. It does not continue the discrete
index \(j\) by an unspecified interpolation, estimate \(j/N\ge1/2\),
or control cancellation between different interior indices in a
mixed word. Those obligations remain in the global source problem.

Run `python3 experiments/check_complete_boundary_coefficient_asymptotic.py`.
The checker verifies the recurrence and normalization identities and
compares the asymptotic with the original finite products. These
finite comparisons are diagnostics; the full-level and uniform claims
follow from the contour argument above.
