# Certified contours for degree two and powers three through thirty-one

Research note, 3 November 2026. This note supplies the finite collection
of phase inequalities needed for the full two-boundary sources with
degree two and \(3\le n\le31\). It uses one parameterized procedure,
with the same wire interval and angular cutoff at every power:
\[
       \alpha=\frac1{32},\qquad \beta=\frac{15}{32},
       \qquad T=\frac{2\pi}{3}.
       \tag{1}
\]
The finite-source interpretation is the trace-first construction in
[the scaled contour lifting theorem](research_scaled_wire_contour_lifting.md).
In particular the certificate includes its angular connectors and
independently raised wire endpoints. It does not certify an arbitrary
simultaneous-height homotopy.

## 1. Phase, saddle and logarithmic branches

Let \(b(x,t)\) be the literal continued Newton phase defined in
Section 1 of
[the three-crossing phase note](research_terminal_three_central_phase.md).
The phase used here is
\[
 \Psi_n(x,t)=2\{b(x,t)+b(x,0)\}
                         +\frac{int^2}{4\pi}-it.
 \tag{2}
\]
The factor two multiplies the wire phases, not the single angular
charge. For an upper or lower wire the primitives \(J_+\), \(J_-\)
have exactly the sides specified in that note. These sides are
retained when a denominator factorial has negative real argument.

The selected point has a useful algebraic description. Define
\[
 p_n(r)=2r^n(r^4-1)-(r^4+1)(r^{2n}+1).
 \tag{3}
\]
For each of the integers \(3,\ldots,31\), the verifier records a
rational complex center \(r_{0,n}\) and proves that the disk of
radius \(2^{-100}\) about it contains exactly one zero \(r_n\).
Put
\[
        t_n=-4i\log r_n,\qquad
        x_n=\frac1\pi\arctan\bigl(\cos(t_n/2)\bigr),
        \qquad h_t=-\Im t_n,\quad h_x=\Im x_n.
        \tag{4}
\]
The logarithm and arctangent are their principal branches on the
recorded disks. Interval arithmetic verifies
\[
\begin{gathered}
 0<\Re t_n<\min(2\pi/n,\pi/2),\qquad \Im t_n<0,\qquad
 \alpha<\Re x_n<\beta,\\
 h_t/(2\pi)>h_x>0,\qquad
 \frac12-\Re x_n-\frac{\Re t_n}{2\pi}>0.
\end{gathered}
 \tag{5}
\]
The final inequality puts every factorial argument at the selected
point strictly inside its ordinary bulk. The wider contour may leave
that bulk; its reciprocal-factorial continuation is still retained.

Here is why this specifies an unexponentiated critical point.
Equation (3), with \(r=e^{it/4}\), gives
\[
                 \tan(t/2)=-i\cos(nt/4).
 \tag{6}
\]
For \(A=i(nt/4-\pi/2)\), inequalities (5) give
\(\Re A>0\), \(-\pi/2<\Im A<0\), and
\(\sinh A=\tan(t/2)\). This is the injective principal strip of
the inverse hyperbolic sine. Hence
\[
                \operatorname{arsinh}(\tan(t/2))
                             =i(nt/4-\pi/2).
 \tag{7}
\]
Also \(\tan(\pi x)=\cos(t/2)\) by (4).

These equations imply the exponentiated wire and trace equations
for (2). To fix their logarithms explicitly, the verifier evaluates
the continued derivatives and proves
\[
                    |\Psi_{n,x}|<1/100,\qquad
                    |\Psi_{n,t}|<1/100
                    \quad\hbox{on the root enclosure}.
 \tag{8}
\]
For example, writing \(k=\tan(\pi x)=\cos(t/2)\) in the derivative
of \(b(x,t)+b(x,0)\) gives
\(\exp(\Psi_{n,x}/2)=1\). Its possible logarithmic values are
integer multiples of \(4\pi i\), so (8) gives \(\Psi_{n,x}=0\).
Likewise the sine-ratio formula for \(b_t\), followed by (7), gives
\(\exp(2\pi\Psi_{n,t})=1\). Its possible values are integer
multiples of \(i\), again excluded by (8) unless zero.
Thus stationarity is exact, not inferred from a small numerical
residual.

The numerical root finder only proposes \(r_{0,n}\). Acceptance
uses the exact Taylor polynomial
\(p_n(r_{0,n}+z)=\sum_j a_jz^j\) and the strict outward bound
\[
              |a_0|+\sum_{j\ge2}|a_j|\rho^j
                           <|a_1|\rho,\qquad \rho=2^{-100}.
 \tag{9}
\]
Rouché's theorem proves that the disk contains one simple zero.
All coefficients of (3) are integers, and the proposed center is
replaced by an exact rational complex midpoint before (9) is tested.

## 2. The complete list of certified surfaces

Write \(M_n=\Re\Psi_n(x_n,t_n)\). The upper main rectangle is
\[
 x=\xi+ih_x,\quad t=\tau-ih_t,\qquad
                   \alpha\le\xi\le\beta,\quad 0\le\tau\le T.
 \tag{10}
\]
For each power the report specifies a rational rectangle \(Q_n\)
in the coordinates \((\xi,\tau/(2\pi))\), strictly containing the
selected point. On all of \(Q_n\), a \(24\)-by-\(24\) subdivision
proves that the real Hessian is negative definite. Outside \(Q_n\),
the certificate proves a gap of at least \(10^{-7}\).
Stationarity and strict concavity on \(Q_n\) therefore show that
(10) has the unique maximum \(M_n\).

The other certified bounds are as follows. Each displayed penalty
is subtracted from the real part of the scaled phase \(\Psi_n\).

| Surface | Domain | Penalty | Certified gap |
|---|---|---|---|
| Negative-angle upper wire | \(x=\xi+ih_x,\ -T\le\tau\le0,\ t=\tau-ih_t\) | \(0\) | \(1/(100n^2)\) |
| Lower wire on the bottom trace | \(x=\xi-ih_x,\ |\tau|\le T,\ t=\tau-ih_t\) | \(4\pi h_x\) | \(1/(100n^3)\) |
| Angular cutoff, upper wire | \(x=\xi+ih_xs,\ t=\pm T-ih_ts\) | \(0\) | \(1/1000\) |
| Angular cutoff, lower wire | \(x=\xi-ih_xs,\ t=\pm T-ih_ts\) | \(4\pi h_xs\) | \(1/1000\) |
| Bottom wire endpoint | \(x=e+\epsilon ih_xv,\ t=\tau-ih_t\) | \(4\pi h_xv\,\mathbf1_{\epsilon=-1}\) | \(1/1000\) |
| Nested endpoint on angular cutoff | \(x=e+\epsilon ih_xvs,\ t=\pm T-ih_ts\) | \(4\pi h_xvs\,\mathbf1_{\epsilon=-1}\) | \(1/1000\) |

Here \(\xi\in[\alpha,\beta]\), \(e\in\{\alpha,\beta\}\),
\(|\tau|\le T\), \(\epsilon=\pm1\), and \(s,v\in[0,1]\).
The signs in the last row are independent. Counting the main
rectangle gives nineteen separate two-dimensional domains.

The lower-wire penalty is twice its actual finite-sum penalty
because (2) is a scaled one-wire phase. For the actual two-wire
source,
\[
 \Re\mathcal F(x_1,x_2,t)-p_1-p_2
       =\frac12\sum_{j=1}^2
                    \{\Re\Psi_n(x_j,t)-2p_j\}.
 \tag{11}
\]
Consequently one nonprincipal wire with scaled gap \(\delta\)
gives an actual gap at least \(\delta/2\); a factor of two is
neither lost nor assigned to the common angular charge.

In the nested endpoint row both \(s\) and \(v\) vary independently.
The new verifier uses direct interval evaluation of \(sv\).
No derivative approximation omits the mixed product or its penalty.
The obsolete family with an interior real trace angle and an
independently decreasing angular height is not among these surfaces:
the trace-first identity never generates it.

## 3. Tail comparisons and finite-factorial input

The report also proves, for every tested power,
\[
 M_n-M_\infty-2g(1/32)>\frac14,\qquad M_n>\frac95,
 \tag{12}
\]
where
\[
 g(x)=J(2x)-4J(x),\qquad M_\infty=2g(1/4)=4G/\pi.
\]
The first inequality removes every original assignment with a wire
outside (1), using the complete Hermite norm of that wire and the
unrestricted bound for the other. This includes high indices and
first normals. It is a bound on the original terms before applying
any contour identity.

The termwise real-angle theorem gives
\(\psi(2\pi/3,0)<4/5\) uniformly for every retained wire subset
and real outside angle. Thus the original outer trace nodes have
rate at most \(2\psi(2\pi/3,0)<8/5<M_n\), including their first
normals by Markov's inequality. The more general proof is recorded
in [the all-degree angular estimate](research_all_degree_outer_angle_gap.md).

The exact Newton factorial interpolation is holomorphic on the
required wire rectangles. A denominator argument with negative real
part is handled by the continued reciprocal factorial, not by
discarding a term of its reflection formula. On our domains its
smallest possible normalized real part is
\[
                  \frac12-\beta-\frac{T}{2\pi}
                           =-\frac{29}{96}>-\frac12.
 \tag{13}
\]
The existing uniform factorial bounds cover this range, including
the limiting zero. Near the selected point the last inequality of
(5) supplies the ordinary nonzero bulk expansion. The parent
factorials remain regular on a small complex bidisk, and their exact
real-boundary estimate supplies positive angular loss on every
listed wire surface.

These observations verify the finite inputs separately from the
phase calculation. The trace-first lifting theorem then retains
every wire correction, angular charge and endpoint current. It
gives a full two-boundary source with factor \(N^{-3/2}\), its
nonzero holomorphic amplitude, and its whole Gaussian strip.
Negative powers follow by coefficient conjugation. This supplies
the missing finite range between the separate power-two theorem
and the existing \(|n|\ge32\) result.

## 4. What the certificate checks

The verifier is
[certify_internal_degree_two_contours.py](../experiments/certify_internal_degree_two_contours.py).
It uses the already audited interval primitives and Taylor covering
engine from the terminal-three certificate. It replaces the phase,
gradient, Hessian, algebraic saddle and wire penalties by their
degree-two formulas. All nested endpoint boxes use direct bounds.

Each parameter rectangle is either accepted by a strict outward
upper bound, accepted inside the separately verified local Hessian
rectangle, or subdivided into two rational rectangles. Success means
that a finite collection covers the entire initial domain. A
floating-point optimizer is never used for acceptance. A numerical
root proposal is accepted only after (9). The report records every
accepted box, every root enclosure, the local Hessian bounds and
the exact script hashes.

The single final report is
[research-internal-degree-two-contours.json](../repro/results/research-internal-degree-two-contours.json).
It covers all twenty-nine integer powers and all \(29\cdot19=551\)
surface domains. To reproduce it:

    python3 experiments/certify_internal_degree_two_contours.py \
      --powers 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 \
               18 19 20 21 22 23 24 25 26 27 28 29 30 31 \
      --precision 180 \
      --output repro/results/research-internal-degree-two-contours.json

This is a proof of the stated inequalities using outward arithmetic,
combined with the written contour and finite-source arguments. It
does not prove a theorem for arbitrary adjacent short-filled
subtrees. The marked geometric identification remains the original
isolated-vertex construction, with its primitive periods retained.
