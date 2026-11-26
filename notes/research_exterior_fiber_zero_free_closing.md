# A zero-free closing disk for actual exterior fibers

Private written proof, 19 November 2026.

The finite pivotal fiber in E has a nonzero Gaussian closing on an
explicit class of admissible offsets. The estimate uses the entire
physical interval. A finite cotangent rectangle selects the actual
lattice alias with coefficient one, controls the other aliases, and
allows a fixed complex fugacity disk about the original evaluation
t=1. The physical offsets remain literal integer data throughout.

The class is nonempty for every fixed number k>=2 of exterior crossing
occurrences, and it occurs among the source's honest flows. For k=1
an exact finite identity gives the closing value. The result does not
control the sum over the other source fibers. In particular neither a
geometric assignment of the offsets nor a nonzero global knot period
is assumed or concluded.

The complete directs are E, the exact finite exterior source equation,
and F, the normalized sine-factorial interpolant. All lattice-tail,
contour-selection and nonempty-class arguments are proved below.

## 1. Exact normalization, conjugation, and the quadratic phase

Use E's literal fiber data
\[
 N\ge2,\ d=N-1,\ q=e^{\pi i/N},\ Q=q^2,\quad
 a_i,b_i\in\mathbb Z_{\ge0},\quad \min_i b_i=0,
 \quad K=d-\max_i(a_i+b_i)\ge0,
 \qquad 1\le i\le k.
 \tag{1}
\]
The sign \(\varepsilon=\pm1\) is the actual common sign on the
rightmost exterior circuit. With the full original fiber coefficients,
including that head's pivot, write
\[
 F_{\gamma,\varepsilon}(t)=\sum_{l=0}^{K}T_{\gamma,l}t^l,
 \qquad S_n=\prod_{j=1}^n2\sin(\pi j/N).
 \tag{2}
\]
The remaining-state label gamma and its exact initial coefficient
\(T_{\gamma,0}\) are retained. In particular it is not replaced by
one. E's coefficient ratio gives, exactly,
\[
 \frac{T_{\gamma,l}}{T_{\gamma,0}}=v_l q^{\varepsilon\Theta_l},
 \quad v_l=\prod_i
       \frac{S_{a_i+b_i+l}S_{b_i}^2}
            {S_{a_i+b_i}S_{b_i+l}^2}>0,
 \tag{3}
\]
\[
 \Theta_l=\frac{k l(l-1)}2+
       l\left[\sum_i b_i-\sum_i a_i+\frac{k(1-d)}2-2\right]
       =\frac{k l^2}2+l\left[\sum_i b_i-\sum_i a_i-\frac{kd}2-2\right].
 \tag{4}
\]
Indeed the positive sine ratio has phase
\(q^{\sum b_i-\sum a_i+kl+k(1-d)/2-2}\), and the negative
ratio is its inverse phase, with the same positive magnitude.
This also follows directly from E(12)--(14). The terms involving
d and the final -2 are respectively the actual finite head and pivot.

Thus the two normalized polynomials with the same integer offsets obey
\[
 \frac{F_{\gamma,-}(t)}{T_{\gamma,0}^{-}}
       =\overline{\frac{F_{\gamma,+}(\bar t)}{T_{\gamma,0}^{+}}}.
 \tag{5}
\]
The initial phases on the two sides need not coincide; (5) is a
statement about their normalized coefficient data. It is not Hermitian
positivity of the original closing.

There is no generic rotated-real-rooted shortcut. If K>=2 and N>k,
the ratio of coefficients numbered 2,0 to the square of coefficient1
in (3) is a positive real number times \(q^{\varepsilon k}\), which
is not real. Multiplying the polynomial by a scalar and rotating t
cannot change that ratio. Consequently its coefficients cannot all
be made real by those operations, as would be necessary for all its
zeros to lie on a rotated real line. The zero-free disk proved below
uses the actual quadratic phase instead.

For the precise asymptotic normalization set
\[
 \mathcal E_{\gamma,N}=T_{\gamma,0}
                  \prod_i\frac{S_{b_i}^2}{S_{a_i+b_i}},
 \quad A_i=\frac{a_i}{N},\quad B_i=\frac{b_i}{N},
 \quad \kappa_N=1-\max_i(A_i+B_i).
 \tag{6}
\]
Every factor in \(\mathcal E_{\gamma,N}\) is literal and nonzero.
The physical upper endpoint is \(K/N=\kappa_N-1/N\), not
\(\kappa_N\). Formula (3) becomes
\[
 T_{\gamma,l}=\mathcal E_{\gamma,N}
    \prod_i\frac{S_{a_i+b_i+l}}{S_{b_i+l}^2}
    \exp\{i\varepsilon N\phi_N(l/N)}
    \exp\{i\varepsilon\pi(k/2-2)l/N\},
 \tag{7}
\]
where
\[
 \phi_N(y)=\pi\left[\frac{k y^2}{2}
           +y\left(\sum_i B_i-\sum_i A_i-\frac k2\right)\right].
 \tag{8}
\]
In particular the subprincipal factor in (7) is not removed by
replacing d by N. Normalizing instead by \(T_{\gamma,0}\) requires
the additional exact product in (6); it can change exponential rates
and powers of N.

## 2. A checkable criterion on the full interval

For real scaled data A,B define
\[
 J(x)=\int_0^x\log(2\sin\pi v)\,dv,\qquad
 R_{A,B}(y)=\sum_i[J(A_i+B_i+y)-2J(B_i+y)],
 \quad 0\le y\le\kappa=1-\max_i(A_i+B_i).
 \tag{9}
\]
The integral is continuous at both ends of [0,1]. In a protected
complex neighborhood of an interior point, its mark is continued
from the positive real sine, exactly as in F.

Fix base data \((A^*,B^*)\) satisfying
\[
 A_i^*>0,\quad B_i^*\ge0,\quad \min_iB_i^*=0,
 \quad A_i^*+B_i^*<1,
 \qquad \cot^2(\pi A_i^*)<8\quad\text{for every }i.
 \tag{10}
\]
Let \(y_0\) be the maximum of (9), whose uniqueness and interior
location are proved just below. The resonance criterion is the
explicit scalar equation
\[
 \pi\left[k y_0+\sum_iB_i^*-\sum_iA_i^*-\frac k2\right]
                         =2\pi n,\qquad n\in\mathbb Z.
 \tag{11}
\]
Equivalently \(y_0\) solves the actual sine-ratio equation
\[
          \prod_i 2\sin\pi(A_i^*+B_i^*+y_0)
                     =\prod_i[2\sin\pi(B_i^*+y_0)]^2,
 \tag{12}
\]
together with (11). No source coefficient is assumed in these tests.

Here is the global concavity proof. For one summand, put
\(c=\cot(\pi A_i)\) and \(v=\cot\pi(B_i+y)\). On its full
physical open interval,
\[
 c+v=\frac{\sin\pi(A_i+B_i+y)}
            {\sin\pi A_i\sin\pi(B_i+y)}>0,
 \qquad
 R_i''(y)=-\pi\frac{2v^2+cv+1}{c+v}.
 \tag{13}
\]
The numerator is positive for all real v when \(c^2<8\).
With a fixed margin in (10) it is bounded below by a positive
constant times \(1+v^2\), while \(c+v\le C(1+|v|)\).
Thus \(R''\le-c_1<0\) on the entire interval, uniformly in a
small admissible real neighborhood of the base data.
At y=0 a denominator with \(B_i=0\) gives \(R'(0+)=+\infty\).
At \(y=\kappa\) an active numerator gives
\(R'(\kappa-)=-\infty\); its denominator is at \(1-A_i\),
strictly between zero and one. Hence the maximum is unique,
interior, and given by (12). It and a fixed neighborhood of it
remain uniformly separated from all factorial walls under small
admissible perturbations. Strong concavity supplies a uniform
strict gap on the rest of the full interval.

## 3. Actual closing theorem and normalization

Assume (10)--(11). There exist a real-data neighborhood \(\mathcal U\),
a disk \(|t-1|<r\), and \(N_0\), such that the following holds for
every N>=N0 and every literal admissible fiber (1) whose exact
scaled data \((A,B)=(a/N,b/N)\) belong to \(\mathcal U\).
The base parameters are not substituted for these exact scaled data.

For the positive sign define
\[
 \Psi_N(y,t)=R_{A,B}(y)+i\phi_N(y)-2\pi i n y+y\operatorname{Log}t,
 \tag{14}
\]
where \(\operatorname{Log}1=0\). There is a unique critical point
\(y_N(t)\) in a fixed neighborhood of \(y_0\). It is holomorphic
in t, and
\[
 H_N(t)=-\partial_y^2\Psi_N(y_N(t),t),
                    \qquad \operatorname{Re}H_N(t)>c_2>0.
 \tag{15}
\]
Use the square root of H with positive real part. Put
\[
 \mathcal A_N(y)=e^{i\pi(k/2-2)y}
       \prod_i\frac{\sqrt{2\sin\pi(A_i+B_i+y)}}
                       {2\sin\pi(B_i+y)},
 \tag{16}
\]
with the square roots continued from positive real values. Then
\[
 \boxed{\quad
 F_{\gamma,+}(t)=\mathcal E_{\gamma,N}
      N^{(1-k)/2}e^{N\Psi_N(y_N(t),t)}
       \left[\frac{\sqrt{2\pi}\,\mathcal A_N(y_N(t))}
                         {\sqrt{H_N(t)}}+O(N^{-1})\right].
 \quad}                                                       \tag{17}
\]
The error is uniform and holomorphic on a slightly smaller disk.
The displayed coefficient is bounded above and away from zero,
uniformly over these actual offsets. Consequently \(F_{\gamma,+}\)
has no zeros on that disk for all sufficiently large N.
Conjugation (5) gives the same conclusion and the conjugated
formula for the negative sign, with its own exact factor
\(\mathcal E_{\gamma,N}\).

In particular this is a nonzero estimate at the original pivotal
evaluation t=1, not at an adjustable closing weight. Its fixed
holomorphic t-jets follow by Cauchy estimates on smaller disks.
For example the logarithmic clock observation satisfies
\[
       \frac1N t\partial_t\log
              \frac{F_{\gamma,+}(t)}{\mathcal E_{\gamma,N}}
                       =y_N(t)+O(N^{-1}).
 \tag{18}
\]
These derivatives are the actual fugacity moments from E, not
meridian normals. No holomorphic continuation of the integer offset
parameters, and no absence of their off-lattice poles, is required.

## 4. Whole physical tails and the exact interpolated central sum

First, uniformly for all \(0\le j\le d\),
\[
                     \log S_j=NJ(j/N)+O(\log(N+1)).
 \tag{19}
\]
For j<=N/2, subtract \(\log v\) from \(\log(2\sin\pi v)\).
The remainder has bounded derivative on [0,1/2]. Integral comparison
for \(\sum\log j\), and the ordinary Riemann estimate for that
remainder, prove (19). For larger j use \(S_jS_{d-j}=N\),
\(J(1-v)=-J(v)\), and the bound
\(\int_0^{1/N}|\log v|\,dv=O(\log N/N)\).
Thus the finite d shift and all endpoints in (19) are included.

Choose a small fixed central interval about \(y_0\). On the
complement of a slightly smaller interval, (13) and (19) bound the
literal sum in (7), after division by \(\mathcal E_{\gamma,N}\), by
\[
           N^{C_3}\exp\{N(R_{A,B}(y_{\rm max})-g)\},
                                                    \qquad g>0,
 \tag{20}
\]
at t=1. A sufficiently small fixed \(|\operatorname{Log}t|\)
preserves a strict gap. This estimate uses only actual lattice
values, up to the physical endpoint \(K/N=\kappa_N-1/N\).
No interpolation past a factorial endpoint is used.

On the central interval every argument \(A_i+B_i+y\) and
\(B_i+y\) lies in a fixed compact subinterval of (0,1). F's
exact sine interpolant \(G_N\) therefore gives a holomorphic
interpolant \(f_N(y,t)\) of the actual summands divided by
\(\mathcal E_{\gamma,N}\): replace each S in (7) by G at its
unchanged affine argument, retain both exponential factors there,
multiply by \(e^{-2\pi i nNy}e^{Ny\operatorname{Log}t}\).
The alias factor is one at every original point y=l/N, and the
last factor is the literal \(t^l\). On a fixed
complex rectangle around the central interval, F proves
\[
 f_N(y,t)=N^{-k/2}e^{N\Psi_N(y,t)}
                \bigl(\mathcal A_N(y)+O(N^{-1})\bigr).
 \tag{21}
\]
The remainder and fixed derivatives are uniformly controlled on
smaller rectangles. All Gamma arguments stay in F's protected
strip there. Equation (21) uses the exact normalized interpolant,
not a chosen solution of the difference equation in E.

## 5. Finite cotangent selection and all alias errors

Here are the contour choices in their required order. At the base
point \(\Psi_y(y_0,1)=0\), and its real-axis quadratic part has
strictly negative real part by (13). Choose the central half-width
\(\eta>0\) small enough that all factorial arguments remain
protected and
\[
                  |\phi_*'(y)-2\pi n|<\pi/4
 \tag{22}
\]
on that real interval. On its two end neighborhoods there is a fixed
real gap. Next choose a height h>0 small compared with that gap
and with \(\eta^2\). Finally shrink the real offset neighborhood
and the t-disk. On the two vertical sides the real part of Psi
then stays below the critical value by a fixed amount. On the
horizontal sides, (22), Taylor's theorem in height, and this final
parameter shrink give
\[
  \sup\operatorname{Re}\Psi_N(y,t)
           -\operatorname{Re}\Psi_N(y_N(t),t)<\pi h.
 \tag{23}
\]
For example the height variation is bounded by
\(h\sup|\phi_N'-2\pi n+\operatorname{Im}\operatorname{Log}t|
   +C h^2\); the small displacement of the critical value is
absorbed by the last parameter choice. The strong real gap in
(20) is preserved by the same ordered choices.

Take the vertical sides at half-grid points
\(u_N=(m_- -1/2)/N\), \(v_N=(m_+ +1/2)/N\), within O(1/N)
of these fixed ends. The rectangle \(\mathcal R_N\), of heights
\(\pm h\), encloses exactly the chosen central physical lattice
points. The residue identity is exact:
\[
 \sum_{l=m_-}^{m_+}f_N(l/N,t)
    =\frac1{2\pi i}\int_{\partial\mathcal R_N}
                            \pi N\cot(\pi Ny)f_N(y,t)\,dy.
 \tag{24}
\]
On either vertical side \(|\cot(\pi Ny)|\le1\): it is a shifted
hyperbolic tangent. Their integrals have a strict exponential gap.
On the top and bottom,
\[
 \cot(\pi N(x+ih))=-i+O(e^{-2\pi Nh}),\qquad
 \cot(\pi N(x-ih))= i+O(e^{-2\pi Nh}).
 \tag{25}
\]
The bound (23) makes both remainders exponentially smaller than
the critical exponential. These exact remainders include all
nonselected local Fourier aliases; none is assigned coefficient zero
by a formal phase argument.

The constant terms in (25), with the counterclockwise rectangle
orientation, give
\[
          \frac N2\left(\int_{u_N}^{v_N}f_N(x+ih,t)\,dx
                       +\int_{u_N}^{v_N}f_N(x-ih,t)\,dx\right).
 \tag{26}
\]
Both integrals can be translated, inside the same analytic rectangle,
to the horizontal segment through \(y_N(t)\). Their vertical
connectors lie on the same gapped sides. Thus (26) equals N times
that single integral, up to an exponentially smaller error. This
proves its coefficient is exactly +1. It uses the actual finite
residue cycle, not an assigned thimble coefficient.

On the translated segment \(\operatorname{Re}\Psi''<-c_2\)
after a further harmless shrink of the rectangle. Taylor expansion
at \(y_N(t)\) therefore yields
\[
 \int f_N(y,t)\,dy
   =N^{-(k+1)/2}e^{N\Psi_N(y_N(t),t)}
       \left[\frac{\sqrt{2\pi}\mathcal A_N(y_N(t))}
                         {\sqrt{H_N(t)}}+O(N^{-1})\right].
 \tag{27}
\]
For completeness, localize on the translated line to a symmetric
\(N^{-2/5}\) interval; its complement has a Gaussian exponential
loss. Expand the analytic amplitude and exponential through the
first nonzero even corrections. Odd terms integrate to zero on
that interval, while the quartic term and square of the cubic term
are O(1/N) after Gaussian scaling. Cauchy bounds on the fixed
rectangle control the remainder. The complex Gaussian integral is
\(\sqrt{2\pi/H_N}\), continued from positive real H; its real
part remains positive, so no orientation or square-root reset occurs.

Multiplying (27) by N, restoring \(\mathcal E_{\gamma,N}\), and
adding (20) proves (17). The neighborhood choices ensure every removed
cap, connector and alias contribution is exponentially smaller than the
leading term. All estimates are uniform on a slightly larger
t-disk than the one asserted. Cauchy's formula gives the stated
holomorphic relative errors and fixed jets.

## 6. Nonempty actual data for every k>=2

This construction concerns one general boundary coefficient, not a
choice of knot or braid family. For every fixed integer k>=2 put
\[
       m=\lceil k/4\rceil,\qquad t_0=\frac12-\frac{2m}{k},
       \qquad -\frac12\le t_0\le0.
 \tag{28}
\]
Take all \(B_i^*=0\) and all \(A_i^*=a\). Seek a maximum with
\(y-a=t_0\). Let \(\delta=-\pi t_0\), \(x=2\pi y\). The
magnitude equation is precisely
\[
             \sin(x+\delta)+\cos x=1,
          \qquad \pi/3\le x\le\pi/2,
          \quad 0\le\delta\le\pi/2.
 \tag{29}
\]
At the two x endpoints its left side minus one has opposite signs.
Its x derivative \(\cos(x+\delta)-\sin x\) is strictly negative
throughout this rectangle. Hence there is a unique root.
At that root \(x+\delta\ge\pi/2\): otherwise
\(\sin(x+\delta)\ge\sin x\) and
\(\sin x+\cos x>1\), except at the initial endpoint.
Implicit differentiation gives
\[
 \frac{dx}{d\delta}=
       \frac{\cos(x+\delta)}{\sin x-\cos(x+\delta)}\in[-1,0].
 \tag{30}
\]
Thus \(a=(x/2+\delta)/\pi\) increases from 1/4 to 2/3,
while \(x+\delta\) increases from \(\pi/2\) to \(5\pi/6\).
In particular
\[
 \frac16\le y\le\frac14,\qquad
 \frac14\le a\le\frac23,\qquad 1-a-y\ge\frac16.
 \tag{31}
\]
The cotangent inequality in (10) consequently has a strict uniform
margin. Equation (29) is exactly
\(\sin\pi(a+y)=2\sin^2\pi y\), so it gives (12).
The actual phase derivative is
\(\phi'(y)=\pi k(y-a-1/2)=-2\pi m\), proving (11) with n=-m.
Equivalently its positive tangent root is
\[
 \tan(\pi y)=
 \frac{\cos(\pi t_0)+\sqrt{1-2\sin(\pi t_0)}}
      {2-\sin(\pi t_0)}.
 \tag{32}
\]
All branches and interval bounds have been fixed by (29).

These bases occur in the honest flow polytope of every diagram with
such a rightmost circuit. For the positive sign first set all u charges
to a common integer near Na and all z charges to a common integer near
Ny. Every conservation law then holds. Subtract that latter integer
only on the rightmost moving z cycle; its b-permutation cycles that
same set, so conservation remains exact. This gives its canonical
representative with all rightmost \(b_i=0\), all \(a_i\) equal to the
chosen integer, and the outside z charges still fixed near Ny.
For the negative sign exchange u,z and use the a-cycle.
For sufficiently large N the caps hold with the margins in (31).
At the actual fiber state near \(l=Ny\), every crossing therefore has
the same charge pair near (a,y), or its exchanged pair. The formula
uses their exact normalized values in (14)--(17), retaining all
rounding phases. Other admissible offsets in the theorem's neighborhood
are covered as well; no analytic continuation of offsets is invoked.

There is a stronger angle-compatible choice for every k>=6. Take m
nearest to k/3 instead of the choice in (28). Then
\[
              \frac27\le\frac mk\le\frac38,\qquad
              -\frac14\le t_0\le-\frac1{14}.
 \tag{32a}
\]
Indeed for k=3r, 3r+1, 3r+2 the nearest integers are respectively
r, r, r+1; in the latter two cases r>=2, giving these bounds.
The proof (29)--(31) is unchanged. Since now
\(0<\delta\le\pi/4\), its root satisfies
\[
       0<y<\tfrac12,\qquad 0<a<\tfrac12,\qquad
                          \tfrac12<a+y<1.
 \tag{32b}
\]
For the upper bound on a use \(y<1/4\) and
\(a=y+\delta/\pi\); for the lower bound on a+y use
\(x+\delta>\pi/2\). Compactness of (32a) gives fixed margins.
Thus the actual whole-diagram state just constructed satisfies the
positive angle inequalities for the five rows
\(a,a,y,y,1-a-y\), at every crossing, with the exchanged assignment
for the negative sign. This is an angle assignment, not a critical
point of the remaining source variables or a geometric holonomy.

## 7. The single-occurrence closing and the outer source

For k=1, the canonical representative has b=0 and K=d-a. E's exact
finite coefficients reduce to
\[
 \frac{F_{\gamma,+}(1)}{T_{\gamma,0}}
       =\sum_{l=0}^{K}Q^{l^2}{K\brack l}_Q\frac1{(Q;Q)_l}
       =\frac1{(Q;Q)_K}.
 \tag{33}
\]
Here is an elementary finite proof of the last identity. The formal
generating function of partitions with largest part at most K is
\(1/(Q;Q)_K\). Classify their Ferrers diagrams by their Durfee
square of side l. The square contributes \(Q^{l^2}\); the part
below it has largest part at most l, contributing \(1/(Q;Q)_l\).
The part to its right fits a rectangle of height l and width K-l.
Its generating polynomial is \({K\brack l}_Q\), as follows by
splitting such rectangle diagrams at their last row, giving the
finite Gaussian Pascal recurrence and its boundary values. This is
a disjoint exhaustive decomposition, proving (33) first as formal
power series and then as a rational identity. Every denominator at
the actual root is nonzero since K<N. Equation (5) gives the
conjugate nonzero value for the negative sign. No fixed zero-free
t-disk for k=1 is inferred merely from this exact value.

Finally, E's original source remains
\[
 K_N=\chi_N\kappa^w(x/s)^{b-1}N^{2c-1}
                         \sum_{\gamma\in\mathfrak B_N}F_\gamma(1).
 \tag{34}
\]
Theorem (17) applies to the specified offset class; every other
gamma still belongs to (34). Even within that class the exact
factors \(\mathcal E_{\gamma,N}\) and their phases remain. A sum
of these nonzero coefficients can cancel. No claim is made that
geometric offsets satisfy (10)--(11), that the other fibers are
lower, or that a short partial filling preserves this neighborhood.
The proved new input is a genuine zero-free disk and a selected
nonzero coefficient for the actual finite boundary polynomial,
with the physical cap and original pivotal evaluation unchanged.

## Complete direct sources

E: notes/research_exterior_pivotal_fiber_quantum_curve.md,
422 lines, SHA256
b214fcb13fcb0eccc42f82597d9eef5aaa77315a2e0014485754df0e3af44fac.

F: notes/exact_factorial_interpolation_and_complex_contours.md,
226 lines, SHA256
1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72.
