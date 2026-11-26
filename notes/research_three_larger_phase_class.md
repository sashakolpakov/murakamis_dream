# A larger analytic phase class with a real output interval

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This extends the proved phase graph transform to a real interval
outside its complex disk, preserving the correlated Schur complement.
It concerns the actual critical phase. A full-source propagation
theorem also requires complementary-integral estimates.

Let \(x_h,k_0,\rho\) have their established values, and put
\[
 R=1/200,\quad W=9/1000,\quad H=13/2000,
 \quad b=9/50,\quad e=13/50,\quad
 D=5+\sqrt{21},\quad
 Z=\frac{(21/20)\rho}{1-(3/10)\rho}.
 \tag{1}
\]
Use the original phase \(\Phi\) of the L40 retained kernel.
Suppose \(S\) is holomorphic near
\(x_h+(\{|z|\le R\}\cup[-W,W])\), with
\[
 S'(x_h+z)/k_0=-\sqrt{21}z+h(z),\qquad
 |h(0)|\le H,\qquad |h'|\le b
 \tag{2}
\]
on that union. Define the actual critical transform
\[
 S_+(x_h+w)=\operatorname{crit}_{z}
                  \{S(x_h+z)+\Phi(x_h+z,x_h+w)\}.
 \tag{3}
\]

**Theorem 1.** The critical point is unique inside \(|z|\le R\)
for every output \(w\) in the stated union, and (3) is holomorphic
on a neighborhood of that union. Write
\(S_+'(x_h+w)/k_0=-\sqrt{21}w+h_+(w)\). Then
\[
 |h_+(0)|\le Z|h(0)|,\qquad
 |h_+'(w)|<
 \begin{cases}4/25,&|w|\le R,\\3/20,&w\in[-W,W].\end{cases}
 \tag{4}
\]
In particular the class (2) is invariant under its analytic transform.
For real output the critical point also satisfies
\[
 |z_c|<.002936,\qquad |z_c-\rho w|<.00106.
 \tag{5}
\]
No incoming function or kernel has been replaced by a quadratic
Gaussian in this statement.

*Proof.* On the complex disk, the existing
[phase-graph theorem](research_three_phase_graph_transform.md)
applies, with the improved incoming derivative bound \(b=.18\).
Its same exact calculation gives
\[
 |h_+'|\le .1+\frac{(2.1)^2}{D-b-.1}-\frac4D<.16,
 \tag{6}
\]
For clarity, subtract the homogeneous quotient before taking absolute
values. If \(|\epsilon|\le e_0=.1\) and
\(|\delta|\le b+e_0\), then
\[
 \left|\frac{(2+\epsilon)^2}{D-\delta}-\frac4D\right|
 \le\frac{4e_0+e_0^2}{D-b-e_0}
       +\frac{4(b+e_0)}{D(D-b-e_0)}
 =\frac{(2+e_0)^2}{D-b-e_0}-\frac4D.
\]
Adding the separate \(e_0\) bound for \(P_{yy}+5\) gives (6).
The original center-gradient contraction remains valid.

For real \(|w|\le W\), symmetry of the original retained phase
and [the analytic Hessian bound](research_three_vertex_input_rectangle.md),
Section 5, give
\[
 |\Phi_{ab}/k_0-\Phi_{ab}(x_h,x_h)/k_0|
       \le18(|z|+|w|)<e\quad (|z|\le R).
 \tag{7}
\]
The relevant homogeneous entries are \(-5,2,-5\).
Writing \(\Phi_x/k_0=-5z+2w+R_x(z,w)\), its critical equation
is exactly
\[
           z=\rho w+\frac\rho2\{h(z)+R_x(z,w)\}.
 \tag{8}
\]
The factor \(\rho/2\) is essential. This is a strict self-map
of the radius-\(R\) disk, with contraction at most
\(\rho(b+e)/2<1/20\). Solving its norm estimate gives
\[
 r_*:=\frac{\rho(1+e/2)W+(\rho/2)H}{1-\rho(b+e)/2}<.002936,
 \qquad
 |z_c-\rho w|\le\frac\rho2\{H+eW+(b+e)r_*\}<.00106.
 \tag{9}
\]
Thus all these critical points belong to the following three-real-
parameter box:
\[
 w\in[-.009,.009],\qquad z=\rho w+\xi+i\eta,
                       \quad |\xi|,|\eta|\le.00106.
 \tag{10}
\]
The exact implicit derivative and the retained Hessian are holomorphic
there. These branches agree with the existing disk branch on their
overlap, by the uniqueness in (8).

To estimate the outgoing derivative, put
\(P_{ab}=\Phi_{ab}/k_0\). The exact Schur formula is
\[
 h_+'=P_{yy}+\sqrt{21}
           -\frac{P_{xy}^2}{P_{xx}-\sqrt{21}+h'(z_c)}.
 \tag{11}
\]
The incoming unknown contributes at most
\[
 \frac{|P_{xy}|^2b}
 {|P_{xx}-\sqrt{21}|\bigl(|P_{xx}-\sqrt{21}|-b\bigr)}.
 \tag{12}
\]
Crucially, retain the cancellation in the known part
\[
           B(z,w)=P_{yy}+\sqrt{21}
                      -\frac{P_{xy}^2}{P_{xx}-\sqrt{21}}.
 \tag{13}
\]
It vanishes exactly at homogeneity. Independent absolute estimates
of its three terms would not prove (4).

An outward cover of all of (10) by 300 rational boxes proves
\[
 |B(z,w)|+
 \frac{|P_{xy}|^2b}
 {|P_{xx}-\sqrt{21}|\bigl(|P_{xx}-\sqrt{21}|-b\bigr)}
                         <3/20.
 \tag{14}
\]
On each complete box, the value of (13) is enclosed at its center
plus its exact holomorphic mean-value enclosure. The three real
derivatives are \(\rho B_z+B_w,B_z,iB_z\). Their expressions
come from the original rational root/Hessian formulas by exact
forward differentiation, including the derivative of the selected
square root. The perturbation (12) is enclosed directly, and every
denominator is separated from zero. The exact binary-tree cover
checks multiplicity and exhaustion of the full parameter box.
Equations (11)--(14) give the real-interval estimate in (4).
All bounds are strict, so the implicit branches and the estimates
continue to fixed neighborhoods. \(\square\)

Run

```sh
python3 experiments/certify_three_real_output_phase_schur.py --precision 192
```

The [checker](../experiments/certify_three_real_output_phase_schur.py)
and [record](../repro/results/research-three-real-output-phase-schur.json)
contain the 300-box Schur cover, all scalar self-map and radius
comparisons, and their proof dependencies. The actual retained source
is separately supplied by
[the union-domain packet](research_three_vertex_real_input_union.md).
Neither that source input nor the present analytic invariant class
by itself bounds a complementary Fourier integral.
